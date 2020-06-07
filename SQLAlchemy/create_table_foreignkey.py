from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    school_id = Column(Integer, ForeignKey("school.id"))

    stu2sch = relationship("School", backref='sch2stu')


class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))


engine = create_engine("mysql+pymysql://root:root@192.168.129.128/sqlalchemy?charset=utf8")

Base.metadata.create_all(engine)
