from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey


class Boy(Base):
    __tablename__ = 'boy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), index=True)


class Gril(Base):
    __tablename__ = 'girl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), index=True)

    # 创建关系
    girl2boy = relationship('Boy', secondary='hotel', backref='boy2girl')


class Hotel(Base):
    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True, autoincrement=True)
    boy_id = Column(Integer, ForeignKey('boy.id'))
    girl_id = Column(Integer, ForeignKey('girl.id'))


from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@192.168.129.128:3306/sqlalchemy?charset=utf8")

Base.metadata.create_all(engine)
