# 파일 불러오기

# import students 다른 폴더에 있어서 못 불러옴
from project import students # ***** 다른 폴더의 파일을 불러올 때, from 폴더 import 파일명 으로 해야 함
from project import student

stus = students.Students()
print(len(stus.slist))

s1 = student.Student(1,"홍길동",100,100,99)
stus.add(s1)
stus.add(student.Student(2,"유관순",90,90,91))
stus.print()
print(s1)
print(stus)
