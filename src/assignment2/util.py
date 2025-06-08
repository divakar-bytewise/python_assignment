from collections import namedtuple

def finding_avg(n,attributes):
    total=0
    for student in range(n):
        student_details=namedtuple("student",attributes)
        ID,MARKS,NAME,CLASS=input().split()
        student=student_details(ID, MARKS, NAME, CLASS)
        total+=int(student.MARKS)
    avg=total/n
    return avg
