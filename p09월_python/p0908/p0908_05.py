class Student:
    def __init__(self,no,name,kor,eng,math):
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = (kor+eng+math)/3

    def __str__(self): # 출력함수를 호출하지 않아도 class를 호출하면 아래의 구문을 자동 출력함
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}"

    def cal_total(self):
        self.total = self.kor + self.eng + self.math

    def cal_avg(self):
        self.avg = self.total/3

# --------------------------------------------------------------------------------------------------

stuList = []

s = Student(1,"홍길동",100,100,99)
print(s)

# 점수 수정하면, sum, avg도 함께 변경이 되어야 함

s.kor = 50
s.cal_total()
s.cal_avg()
print(s)

while True:
    no = input("번호:")
    if no == 0: break
    name = input("이름:")
    kor = int(input("국어:"))
    eng = int(input("영어:"))
    math = int(input("수학:"))
    stuList.append(Student(no,name,kor,eng,math))

print("-"*60)
for s in stuList:
    print(s)


# class Students:
#     slist = []
#     # 생성자 : 객체선언 시 실행됨
#     def __init__(self,s):
#         self.slist.append(s)

#     # 함수 : 함수호출 시 실행됨
#     def add(self,s):
#         self.slist.append(s)

# # --------------------------------------------
# # 객체선언
# # s = Student(1,"홍길동",100,100,99)
# # s2 = Student(2,"유관순",90,90,91)

# # 객체선언
# stu = Students(Student(1,"홍길동",100,100,99))
# stu.add((Student(2,"유관순",90,90,91)))

# for ss in stu.slist:
#     print(ss)

