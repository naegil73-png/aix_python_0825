
class Students:
    slist = []

    def add(self,s):
        self.slist.append(s)

    def print(self):
        print("-"*70)
        print("번호\t이름\t국어\t수학\t영어\t합계\t평균\t등수")
        print("-"*70)
        for s in self.slist:
            print(s) # 양식이 동일한 student의 str함수를 적용