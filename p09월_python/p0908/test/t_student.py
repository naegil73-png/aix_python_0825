class Student:

    def __init__(self,*args):
        if len(args) == 5:
            self.no = args[0]
            self.name = args[1]
            self.kor = args[2]
            self.eng = args[3]
            self.math = args[4]
            self.total = self.kor+self.eng+self.math
            self.avg = self.total/3
            self.rank = 0

        elif len(args) == 8:
            self.no = args[0]
            self.name = args[1]
            self.kor = args[2]
            self.eng = args[3]
            self.math = args[4]
            self.total = args[5]
            self.avg = args[6]
            self.rank = args[7]

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"

    def cal_total(self):
            self.total = self.kor+self.eng+self.math

    def cal_avg(self):
            self.avg = self.total/3

    def s_str(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"