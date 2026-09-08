class Student:
    def __init__(self, no,name,kor,eng,math): # print하면 별도의 함수를 호출하지 않는한, 이구간의 값을 반환한다.
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = self.kor+self.eng+self.math
        self.avg = self.total/3

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}"

    def cal_total(self): # 별도의 함수 지정 : 나중에 함수값의 수정, 함수만 출력 등에 사용 -> 수식은 아래로 적용되기 때문에 별도로 있어야 함
        self.sum = self.kor+self.eng+self.math

    def cal_avg(self):
        self.avg = self.sum/3

s = Student(1,"홍길동",100,100,100)
print(s)

s.name = "임꺽정"
print(s)



# 캡슐화

class Student:
    def __init__(self, no,name,kor,eng,math): # print하면 별도의 함수를 호출하지 않는한, 이구간의 값을 반환한다.
        self.__no = no
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__math = math
        self.total = self.__kor+self.__eng+self.__math
        self.avg = self.total/3

    def __str__(self):
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.total}\t{self.avg}"

    def get__kor(self):
        return self.__kor

    def set_kor(self,kor):
        self.__kor = kor

    def cal_total(self): # 별도의 함수 지정 : 나중에 함수값의 수정, 함수만 출력 등에 사용 -> 수식은 아래로 적용되기 때문에 별도로 있어야 함
        self.sum = self.__kor+self.__eng+self.__math

    def cal_avg(self):
        self.avg = self.sum/3

s = Student(1,"홍길동",100,100,100)
print(s)

s.name = "임꺽정"
print(s)