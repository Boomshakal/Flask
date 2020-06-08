from create_table import engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)

db_session = Session()
