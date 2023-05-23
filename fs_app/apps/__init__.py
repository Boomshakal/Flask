# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : __init__.py.py
# Time       ：2023/5/16 23:24
# Author     ：李慧敏
# Description：
"""

from flask import Flask
from flask_cors import CORS

# 导入Flask-SQLAlchemy中的SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 实例化SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()
"""
数据库迁移指令:
flask db init 
flask db migrate  # Django中的 makemigration
flask db upgrade  # Django中的 migrate
"""
# PS : 实例化SQLAlchemy的代码必须要在引入蓝图之前
from apps.user.view import user


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    CORS(app, resources=r'/*')  # 注册CORS, "/*" 允许访问所有api

    # 初始化App配置 这个app配置就厉害了,专门针对 SQLAlchemy 进行配置
    # SQLALCHEMY_DATABASE_URI 配置 SQLAlchemy 的链接字符串儿
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/flask?charset=utf8"

    # SQLALCHEMY_POOL_SIZE 配置 SQLAlchemy 的连接池大小
    app.config["SQLALCHEMY_POOL_SIZE"] = 5

    # SQLALCHEMY_POOL_TIMEOUT 配置 SQLAlchemy 的连接超时时间
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # 初始化SQLAlchemy , 本质就是将以上的配置读取出来
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user)

    return app
