# "c:/aaa/stu.txt"파일을 읽고, 쓰고, 학생성적 프로그램 메인화면, 입력기능, 출력기능, 수정기능 

title = ["번호","이름","국어","영어"]

def ReadF():
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            str = f.readline()
            if str == "": break
            stu = str.split(',')
            for i,v in enumerate(stu):
                if i == 0 or i == 1: continue
                if 2 <= i <= 5:
                    stu[i] = int(v)
                if i == 6:
                    stu[i] = float(v)

