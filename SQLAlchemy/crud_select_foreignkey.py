from crud import db_session

from create_table_foreignkey import Student, School

# relationship 正向
# stu_list = db_session.query(Student).all()
#
# for stu in stu_list:
#     print(stu.id, stu.name, stu.school_id, stu.stu2sch.name)

# relationship 反向
sch_list = db_session.query(School).all()

for sch in sch_list:
    for student in sch.sch2stu:
        print(student.name)