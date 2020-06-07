from crud import db_session
from create_table import User

db_session.query(User).filter_by(id=3).update({'name': ''})

#在原有值基础上添加 - 1
db_session.query(User).filter(User.id > 0).update({User.name: User.name + '007' }, synchronize_session=False)

#在原有值基础上添加 - 2
# db_session.query(User).filter(User.id > 0).update({"age": User.age + 1}, synchronize_session="evaluate")
db_session.commit()
db_session.close()
