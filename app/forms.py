#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    """docstring for LoginForm"""
    # def __init__(self, arg):
    #     super(LoginForm, self).__init__()
    #     self.arg = arg
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default = True)

class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])