#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# config initialed
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

# db initialed
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from app import views, models