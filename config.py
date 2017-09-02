# OpenID 配置
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
# 引入数据库
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# # 通过电子邮件发送错误
# # mail server settings
# MAIL_SERVER = 'localhost'
# MAIL_PORT = 25
# MAIL_USERNAME = None
# MAIL_PASSWORD = None
# # administrator list
# ADMINS = ['you@example.com']

# 通过电子邮件发送关注提醒
# mail server settings
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# MAIL_USERNAME = 'for_test_jyk@163.com'
# MAIL_PASSWORD = 'fortestjyk13'

MAIL_USERNAME = '601688108@qq.com'
MAIL_PASSWORD = 'bxceufbtnpotbbig'
# administrator list
# ADMINS = ['jiangyukuan13@163.com']
# ADMINS = ['for_test_jyk@163.com','601688108@qq.com']
ADMINS = ['601688108@qq.com']


# pagination分页
POSTS_PER_PAGE = 3

# for search
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50