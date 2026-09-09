# 메인 구성: 관련 모듈을 불러온다. -> 출력, 입력 클래스를 호출 -> 출력문의 함수

from t_student import Student
from t_students import Students

stus = Students()

s1 = Student(1,"홍길동",100,100,100)
s2 = Student(2,"유관순",100,100,100)

stus.add(s1)
stus.add(s2)

stus.s_print()