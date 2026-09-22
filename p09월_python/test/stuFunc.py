from student import Student
from students import Students

stus = Students()
stuNum = 1

def readStu():
    global stuNum
    with open("C:\\aaa\\stu.txt",'r',encoding='utf-8') as f:
        while True:
            str = f.readline()
            if str == "": break
            stu = str.strip().split(',')

            for i, s in enumerate(stu):
                if 0<=i<=1: continue
                elif 2<=i<=5:
                    stu[i] = int(s.strip())
                elif i == 6:
                    stu[i] = float(s.strip())
                elif i == 7:
                    stu[i] = int(s.strip())
            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))
            stuNum = len(stus.slist)+1

def writeStu():
    with open("C:\\aaa\\stu.txt",'w',encoding='utf-8') as f:
        for s in stus.slist:
            str = s.s_str()
            f.write(str+'\n')

def main_screen():
    while True:
        print("-"*70)
        print('[학생성적관리프로그램]')
        print("-"*70)
        print('[1.학생성적입력관리]')
        print('[2.학생성적출력관리]')
        print('[3.학생성적수정관리]')
        print('[9.학생성적저장관리]')
        print('[0.프로그램종료]')

        choice = int(input("작업선택:"))
        return choice

def s_input():
    global stuNum
    while True:
        print('[학생성적입력]')
        no = stuNum
        name = input("학생이름:")
        if name == "0": break
        kor = int(input("국어성적:"))
        eng = int(input("영어성적:"))
        math = int(input("수학성적:"))
        total = kor+eng+math
        avg = total/3
        rank = 0
        stus.add(Student(no,name,kor,eng,math))
        stuNum += 1
        print("성적이 입력되었습니다.")

def s_output():
    stus.print()

def s_update():
    print('[학생성적수정]')
    name = input("수정할 학생이름:")
    temp = 0
    for s in stus.slist:
        if s.name == name:
            temp = 1
            print(f"{name}학생을 찾았습니다.")
            print('[1.국어,2.수학,3.영어]')
            choice = int(input("과목선택(0:이전화면):"))
            if choice == 0:break
            elif choice == 1:
                print(f"{name}학생 국어점수는 {s.kor}점입니다.")
                s.kor = int(input("수정할 국어점수:"))
                print(f"{name}학생 국어점수가 {s.kor}점으로 수정되었습니다.")
            elif choice == 2:
                print(f"{name}학생 영어점수는 {s.eng}점입니다.")
                s.eng = int(input("수정할 영어점수:"))
                print(f"{name}학생 영어점수가 {s.eng}점으로 수정되었습니다.")
            elif choice == 3:
                print(f"{name}학생 수학점수는 {s.math}점입니다.")
                s.math = int(input("수정할 수학점수:"))
                print(f"{name}학생 수학점수가 {s.math}점으로 수정되었습니다.")
            s.s_total()
            s.s_avg()

    if temp == 0:
        print(f"{name}학생은 없습니다.")