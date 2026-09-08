# stuList = []

# # students -> student클래스 생성
# # 홍길동 성적 -> stuList에 넣고 # stuList.append(s1)
# # 유관순 성적 -> stuList.append(s2)

# # 학생성적을 출력하시오.
# # for문을 사용해서 출력하시오.

# # 
# from student import Student
# s1 = Student(1,"홍길동",90,85,100)
# s2 = Student(2,"유관순",90,85,100)

# stuList.append(s1)
# for s in stuList:
#     print(s)



# stus = Students()
# student -> Student 클래스
# 홍길동성적 -> stus.add(s1)
# 유관순성적 -> stus.add(s2)

# stus.print()

# 클래스의 시작
# 1.모듈을 import
from students import Students
from student import Student

# 2.원하는 변수에 전체 출력문 할당
stus = Students()

# 3.개별 입력정보 모듈 호출
s1 = Student(1,"홍길동",100,100,99)
s2 = Student(2,"유관순",100,100,99)

# 5.Student가 실행한 결과를 변수에 더함(문자열)
stus.add(s1) # stus에 add함수를 적용하라. 입력변수는 s1이다.
stus.add(s2) # stus에 add함수를 적용하라. 입력변수는 s2이다. = Student의 결과 합함 -> 떨어진 개별자료 -> 자료명과 자료 묶는 과정이 필요 -> 
# 결과를 하나의 변수로 받아 리스트로 반환, 각 결과물을 순차적으로 출력하기 위해 print의 for문으로 실행 -> students로 이동

stus.print() # 7.stus에 print함수를 적용하라.


