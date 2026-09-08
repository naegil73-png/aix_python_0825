class Students:
    slist = []

    def add(self,s): # 6.main의 add함수에서 연계, slist는 클래스로 묶여서 적용 가능
        self.slist.append(s) # main에서 전달받는 입력변수를 s라고 명하고, 이를 slist에 더하라 

    def print(self):
        print("-"*70)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균") # 자료명은 탭으로 구분
        print("-"*70)
        for s in self.slist: # 자료에 대한 출력양식 -> student를 참고해서 __str__을 적용함
            print(s)