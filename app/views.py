#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
@login_required
def index():
    # return 'Hello World!'
    # user = {'nickname':'Cloud'}
    user = g.user
    posts = [{'author': { 'nickname': 'John' },'body': 'I\'m the 1st one !Beautiful day in Portland!'},
    {'author': { 'nickname': 'Susan' },'body': 'I\'m No.2!The Avengers movie was so cool!'}]
    return render_template('index.html', title = 'Home', user = user, posts = posts)
    
@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # flash('Login requested for OpenID="' + form.openid.data + '",...'''
        #     ' remember_me=' + str(form.remember_me.data))
        # return redirect('/index')
        session['remmeber_me'] = form.remember_me.data
    return render_template('login.html', title = 'Sign In', 
        form = form, providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    # prompt('remember me set:'+ remember_me)
    if 'remember_me' in session:
        # prompt('remember me set:'+ remember_me)
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

    # return '''
    # <html>
    #     <head>
    #         <title>Home Page</title>
    #     </head>
    #     <body>
    #         <h1>hello1,'''+user['nickname']+'''</h1>
    #         <h2>hello2,'''+user['nickname']+'''</h2>
    #     </body>
    # </html>'''