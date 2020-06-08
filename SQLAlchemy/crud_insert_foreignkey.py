from crud import db_session

from create_table_foreignkey import Student, School

# 1. 笨方法
# sch_obj = School(name='hzkj')
# db_session.add(sch_obj)
# db_session.commit()
#
# sch = db_session.query(School).filter(School.name == 'hzkj').first()
# stu_obj = Student(name='lhm', school_id=sch.id)
# db_session.add(stu_obj)
# db_session.commit()
# db_session.close()

# 2.反向添加数据 relationship
# sch_obj = School(name='zjgy')
# sch_obj.sch2stu = [Student(name='lhc')]
# db_session.add(sch_obj)
# db_session.commit()
# db_session.close()

# 3.正向添加数据 relationship
stu_obj = Student(name='liyang', stu2sch=School(name='xdf'))
db_session.add(stu_obj)
db_session.commit()
db_session.close()
