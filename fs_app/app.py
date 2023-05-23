# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : app.py
# Time       ：2023/5/16 23:36
# Author     ：李慧敏
# Description：
"""
import apps

# 导入 Flask-Script 中的 Manager
from flask_script import Manager

app = apps.create_app()
# 让app支持 Manager
manager = Manager(app)  # type:Manager

manager.add_command("db", Manager)


@manager.command
def show(arg):
    print(arg)


@manager.option("-h", "--host", dest="host")
@manager.option("-p", "--port", dest="port")
def run_flask(host, port):
    # print(f"{host}:{port}")
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    # app.run()
    # 替换原有的app.run(),然后大功告成了
    manager.run()
