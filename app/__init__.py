#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# config initialed
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

# db initialed
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app,os.path.join(basedir, 'tmp'))

from app import views, models
