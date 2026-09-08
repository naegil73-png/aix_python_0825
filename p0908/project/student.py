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