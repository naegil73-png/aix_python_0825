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
stus.add(s1) # stus에 s1 = Student의 결과 합함 -> 
stus.add(s2) # stus에 s1 = Student의 결과 합함 -> 각각 떨어진 자료
# 각 자료를 한데 묶는 과정과 자료명도 같이 출력이 필요 -> 
# 각 결과를 하나의 변수로 받아 리스트로 반환, print의 for문으로 실행

stus.print()


