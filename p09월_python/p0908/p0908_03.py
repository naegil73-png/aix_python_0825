# class Student: # 클래스는 첫글자는 대문자
#     # no = 0
#     # name = ""
#     # kor = 0
#     # eng = 0

#     def __init__(self,no,name,kor,eng): # 없는 변수를 입력해도 만들어서 생성함 -> calss Student: 아래의 변수들은 필요없음
#         self.no = no
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.total = kor+eng

# stuList = []

# s = Student(1,"홍길동",100,100)
# stuList.append(s)
# s.kor = 50 # 클래스변수값 수정 : kor변수 = 100이나, 50으로 수정됨(즉, 있는 변수에 값을 넣으면 값 수정)
# s.math = 100 # 클래스변수 추가 : 없는 변수를 입력하면, 변수를 생성해서 입력해줌



class Student: # 클래스는 첫글자는 대문자
    # no = 0
    # name = ""
    # kor = 0
    # eng = 0

    def __init__(self,no,name,kor,eng,math): # 없는 변수를 입력해도 만들어서 생성함 -> calss Student: 아래의 변수들은 필요없음
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = (kor+eng+math)/3

    def __str__(self): # 참조변수가 출력되면, 아래의 문자가 출력됨
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}"

    # 클래스 내 함수 매개변수 앞에 self를 붙여야 함
    def sum(self):
        self.sum = self.kor+self.eng+self.math

    def avg(self):
        self.avg - self.sum/3

    def print(self):
        print(self.no,self.name,self.kor,self.eng,self.math,self.total,f"{self.avg:.2f}",sep="\t")

stuList = []

s = Student(1,"홍길동",100,100,99)
stuList.append(s)
s.kor = 50 # 클래스변수값 수정 : kor변수 = 100이나, 50으로 수정됨(즉, 있는 변수에 값을 넣으면 값 수정)
s.math = 100 # 클래스변수 추가 : 없는 변수를 입력하면, 변수를 생성해서 입력해줌
s.print()


# 변수 캡슐화 : 클래스 내부에서만 값을 수정하려면..

class Student: # 클래스는 첫글자는 대문자
    # no = 0
    # name = ""
    # kor = 0
    # eng = 0

    def __init__(self,no,name,kor,eng,math): # 없는 변수를 입력해도 만들어서 생성함 -> calss Student: 아래의 변수들은 필요없음
        self.__no = no
        self.__name = name
        self.__kor = kor # 캡슐화 : 클래스 내부에서만 수정 가능
        self.__eng = eng
        self.__math = math
        self.total = kor+eng+math
        self.avg = (kor+eng+math)/3

    def __str__(self): # 참조변수가 출력되면, 아래의 문자가 출력됨
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.__total}\t{self.__avg:.2f}"

    # 클래스 내 함수 매개변수 앞에 self를 붙여야 함
    def sum(self):
        self.__sum = self.__kor+self.__eng+self.__math

    def avg(self):
        self.__avg - self.__sum/3

    def print(self):
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math,self.total,f"{self.avg:.2f}",sep="\t")

stuList = []

s = Student(1,"홍길동",100,100,99)
print("-"*60)
stuList.append(s)
print("-"*60)
s.kor = 50 
s.math = 100 
s.print()

# 변수 캡슐화된 상태에서 값을 변경하려면..

class Student: # 클래스는 첫글자는 대문자
    # no = 0
    # name = ""
    # kor = 0
    # eng = 0

    def __init__(self,no,name,kor,eng,math): # 없는 변수를 입력해도 만들어서 생성함 -> calss Student: 아래의 변수들은 필요없음
        self.__no = no
        self.__name = name
        self.__kor = kor # 캡슐화 : 클래스 내부에서만 수정 가능
        self.__eng = eng
        self.__math = math
        self.total = kor+eng+math
        self.avg = (kor+eng+math)/3

    def __str__(self): # 참조변수가 출력되면, 아래의 문자가 출력됨
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.total}\t{self.avg:.2f}"

    def get_kor(self):
        return self.__kor

    def set__kor(self,kor):
        self.__kor = kor

    # 클래스 내 함수 매개변수 앞에 self를 붙여야 함
    def sum(self):
        self.__sum = self.__kor+self.__eng+self.__math

    def avg(self):
        self.__avg - self.__sum/3

    def print(self):
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math,self.total,f"{self.avg:.2f}",sep="\t")

stuList = []

s = Student(1,"홍길동",100,100,99)
print("-"*60)
print(s)
stuList.append(s)
print("-"*60)
s.kor = 50 
s.math = 100 
s.set__kor(50)
s.print()

# --- 캡슐화하게 되면 값을 수정할 수 있도록 setter, getter를 만들어줌 ------------------------------------------------------

class Student:
    # 생성자
    def __init__(self,no,name,kor,eng,math):
        self.__no = no
        self.__name = name
        self.__kor = kor  #캡슐화:클래스내부에서만 값을 수정
        self.__eng = eng
        self.__math = math
        self.__total = kor+eng+math
        self.__avg = (kor+eng+math)/3

    def __str__(self):
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.__total}\t{self.__avg:.2f}"

    def get_kor(self):
        return self.__kor

    def set_kor(self,kor): # 캡슐화를 하면, 잘못된 값이 입력될때 에러처리
        if kor<0:
            print("잘못된 값이 들어옴.")
            return
        self.__kor = kor


    # 클래스 내 함수 매개변수 첫번째 self
    def cal_total(self):
        self.__total = self.__kor+self.__eng+self.__math

    def cal_avg(self):
        self.__avg = self.__total/3

    def print(self):
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math,self.__total,f"{self.__avg:.2f}",sep="\t")

stuList = []
# 객체선언
s = Student(1,"홍길동",100,100,99)
print("-"*50)
print(s)
print("-"*50)
s.__kor = 70    # 클래스 변수값 수정이 안됨(캡슐화)
s.__math = 40   # 클래스 변수값 수정이 안됨(캡슐화)
s.set_kor(-50)  # setter,getter를 사용해서 수정,확인을 해야 함.
s.cal_total()
s.cal_avg()
s.print()
print(s)