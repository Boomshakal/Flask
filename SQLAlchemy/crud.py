from create_table import User, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)

db_session = Session()

# user_obj = User(name='lhm')
## insert_one
# db_session.add(user_obj)
#
# db_session.commit()
# db_session.close()

# insert_many
db_session.add_all([
    User(name='lhc'),
    User(name='wxy'),
    User(name='lgy')
])
db_session.commit()
db_session.close()
