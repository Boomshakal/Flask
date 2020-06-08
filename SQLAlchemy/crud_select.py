from crud import db_session
from create_table import User

# user_list = db_session.query(User).all()
#
# for user in user_list:
#     print(user.name)

# user = db_session.query(User).first()
# print(user.name)

# 条件查询
# user_list = db_session.query(User).filter(User.id == 3).all()
# print(user_list[0].id, user_list[0].name)

# user_list = db_session.query(User).filter(User.id > 3).all()
# print(user_list[0].id, user_list[0].name)

user_list = db_session.query(User).filter_by(id=3).all()
print(user_list[0].id, user_list[0].name)

