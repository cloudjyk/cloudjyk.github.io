#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# config initialed
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

# db initialed
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app,os.path.join(basedir, 'temp'))

from app import views, models
