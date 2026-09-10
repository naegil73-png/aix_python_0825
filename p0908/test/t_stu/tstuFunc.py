from t_student import*
from t_students import*

stus = Students()
stuNum = 1

def readStu():
    global stuNum
    with open("C:\\aaa\\stu.txt",'r',encoding='utf-8') as f:
        while True:
            str = f.readline()
            if str == "":break
            stu = str.split(',')

            for i, v in enumerate(stu):
                if i == 0 or i == 1: continue
                elif 2<= i <= 5:
                    stu[i] = int(v.strip())
                elif i == 6:
                    stu[i] = float(v.strip())
                elif i == 7:
                    stu[i] = int(v.strip())

            stus.add(Student("stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]"))
            stuNum = len(stus)

def writeStu():
    with open("C:\\aaa\\stu.txt",'w',encoding='utf-8') as f:
        for s in stus.slist:
            str = s.s_str()
            f.write(str+'\n')

def main_screen():
    while True:
        print("[학생성적관리프로그램]")
        print("-"*70)
        print("[1.학생성적입력관리]")
        print("[2.학생성적출력관리]")
        print("[3.학생성적수정관리]")
        print("[9.학생성적저장관리]")
        print("[0.프로그램 종료]")

        choice = input("원하는 작업:")
        if not choice.isdigit:
            print("숫자를 입력하세요.")
        else:
            choice = int(choice)
            break

def s_input():
    global stuNum
    while True:
        print("[학생입력관리]")
        no = stuNum
        name = input("이름입력:")
        if name == "0": break
        kor = input("국어성적:")
        eng = input("영어성적:")
        math = input("수학성적:")
        total = kor+eng+math
        avg = total/3
        rank = 0

        stus.add(Student(no,name,kor,eng,math))
        print(f"{name}학생 성적이 저장되었습니다.")
        stuNum += 1

def s_output():
    stus.print()

def s_update():
    print('[학생성적수정]')
    temp = 0
    name = input("학생이름:")
    for s in stus.slist:
        if s.name == name:
            print(f"{name}학생을 찾았습니다.")
            temp = 1
            print('[1.국어,2.영어,3.수학]')
            choice = int(input("수정과목 선택:"))
            if choice == 1:
                print(f"현재 {name}학생 국어성적은 {s.kor}입니다.")
                s.kor = int(input("수정 국어점수:"))
                s.s_total()
                s.s_avg()

    if temp == 0:
        print("{name}학생은 없습니다.")
