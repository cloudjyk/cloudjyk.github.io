#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    # return 'Hello World!'
    user = {'nickname':'Cloud'}
    posts = [{'author': { 'nickname': 'John' },'body': 'I\'m the 1st one !Beautiful day in Portland!'},
    {'author': { 'nickname': 'Susan' },'body': 'I\'m No.2!The Avengers movie was so cool!'}]
    return render_template('index.html', title = 'Home', user = user, posts = posts)
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '",...'''
            ' remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', 
        form = form, providers = app.config['OPENID_PROVIDERS'])



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