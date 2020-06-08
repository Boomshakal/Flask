from crud import db_session
from create_table import User

res = db_session.query(User).filter_by(id=3).delete()
print(res)
db_session.commit()
db_session.close()
