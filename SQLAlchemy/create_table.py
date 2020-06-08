from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), index=True)


from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@192.168.129.128:3306/sqlalchemy?charset=utf8")

Base.metadata.create_all(engine)
