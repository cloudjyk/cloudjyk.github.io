#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    """docstring for LoginForm"""
    # def __init__(self, arg):
    #     super(LoginForm, self).__init__()
    #     self.arg = arg
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default = True)