import MyApp

# 导入 Flask-Script 中的 Manager
from flask_script import Manager

# 导入 Flask-Migrate 中的 Migrate 和 MigrateCommand
# 这两个东西说白了就是想在 Flask-Script 中添加几个命令和指令而已
from flask_migrate import Migrate, MigrateCommand

app = MyApp.create_app()
# 让app支持 Manager
manager = Manager(app)  # type:Manager

# Migrate 既然是数据库迁移,那么就得告诉他数据库在哪里
# 并且告诉他要支持那个app
Migrate(app, MyApp.db)
# 现在就要告诉manager 有新的指令了,这个新指令在MigrateCommand 中存着呢
manager.add_command("db", MigrateCommand)  # 当你的命令中出现 db 指令,则去MigrateCommand中寻找对应关系
"""
数据库迁移指令:
python manager.py db init 
python manager.py db migrate   # Django中的 makemigration
python manager.py db upgrade  # Django中的 migrate
"""


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
