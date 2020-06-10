from sqlalchemy.orm import sessionmaker
from create_table_M2M import engine, Boy, Gril, Hotel

Session = sessionmaker(engine)

db_session = Session()

# 1. 通过Boy添加Girl和Hotel数据relationship 正向
boy = Boy(name='lhm')
boy.boy2girl = [Gril(name='qwe'), Gril(name='asd')]
db_session.add(boy)
db_session.commit()
db_session.close()

# 2. 通过Girl添加Boy和Hotel数据 relationship 正向
girl = Gril(name='zxc', girl2boy=[Boy(name='iop'), Boy(name='jkl')])
db_session.add(girl)
db_session.commit()
db_session.close()

girl_list = db_session.query(Gril).all()
for girl in girl_list:
    for boy in girl.girl2boy:
        print(girl.name, boy.name)

boy_list = db_session.query(Boy).all()
for boy in boy_list:
    for girl in boy.boy2girl:
        print(boy.name, girl.name)
