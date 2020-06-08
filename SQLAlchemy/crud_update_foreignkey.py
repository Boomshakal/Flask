from crud import db_session

from create_table_foreignkey import Student, School

# 修改数据
sch = db_session.query(School).filter(School.name=='xdf').first()
stu = db_session.query(Student).filter(Student.name=='lhc').update({'school_id':sch.id})
db_session.commit()
db_session.close()
