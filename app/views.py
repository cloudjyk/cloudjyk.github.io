#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    # return 'Hello World!'
    user = {'nickname':'Cloud'}
    posts = [{'author': { 'nickname': 'John' },'body': 'I\'m the 1st one !Beautiful day in Portland!'},
    {'author': { 'nickname': 'Susan' },'body': 'I\'m No.2!The Avengers movie was so cool!'}]
    return render_template('index.html', title = 'Home', user = user, posts = posts)



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