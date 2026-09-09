class Students:
    stuList = []

    def add(self,s):
        self.stuList.append(s)

    def s_print(self):
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format("이름","번호","국어","영어","수학","합계","평균"))
        print("-"*60)

        for s in self.stuList:
            print(s)