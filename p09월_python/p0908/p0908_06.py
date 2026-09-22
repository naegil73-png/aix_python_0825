class Student:
    no = 0
    name = ""
    total = 0
    avg = 0

    def __init__(self,no,name,kor,eng,math):
    # def __init__(self): 이렇게 쓸 수도 있으나, 이렇게 쓰면, 위의 3줄을 써야 함

        self.no = no # self를 안쓰면, init구문의 no로 다시 돌아감. self를 넣으면, 위의 no값을 적용함(위의 3줄을 안쓰더라도 자동으로 생성해줌)
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        # self.rank = rank # rank 추가

# 객체선언을 하면,

s1 = Student(1,"홍길동",100,100,100)
s21 = Student(2,"유관순",100,100,100)

# 출력 : 참조변수명.변수명
print(s1.name) # 홍길동을 출력하려면

# 수정 : 참조변수명.변수명 = 수정값
s1.name = "홍길자"
print(s1.name)

# 추가 : 참조변수명.변수명 => 없는 변수 입력 시 추가
s1.rank = 1
print(s1.name)

# 전체 출력
print(s1.no,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,sep="\t") # 이렇게 출력할 수도 있으나...


# --------------------------------------------------------------------------------------

class Student:
    no = 0
    name = ""
    total = 0
    avg = 0

    def __init__(self,no,name,kor,eng,math):
    # def __init__(self): 이렇게 쓸 수도 있으나, 이렇게 쓰면, 위의 3줄을 써야 함

        self.no = no # self를 안쓰면, init구문의 no로 다시 돌아감. self를 넣으면, 위의 no값을 적용함(위의 3줄을 안쓰더라도 자동으로 생성해줌)
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        # self.rank = rank # rank 추가

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}"

    def cal_total(self):
        self.total = self.kor+self.eng+self.math

    def cal_avg(self):
        self.avg = self.total/3

# 객체선언을 하면,

s1 = Student(1,"홍길동",100,100,100)
s2 = Student(2,"유관순",100,100,100)

# 출력 : 참조변수명.변수명
print(s1.name) # 홍길동을 출력하려면

# 수정 : 참조변수명.변수명 = 수정값
s1.name = "홍길자"
print(s1.name)

# 추가 : 참조변수명.변수명 => 없는 변수 입력 시 추가
s1.rank = 1
print(s1.name)

# 전체 출력
print(s1.no,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,sep="\t") # 이렇게 출력할 수도 있으나...
print(s1)
print(s2)

# 변수값 변경 -> 관계된 변수값도 변경
s1.kor = 10
s1.cal_total() # sl.total = s1.kor+s1.eng+s1.math로 할 수도 있으나 번거로움
s1.avg()
print(s1)