from t_student import Student
from t_students import Students

stus = Students()
stuNum = 1

def readStu():
    global stuNum

    with open("C:\\aaa\\stu.txt",'r',encoding='utf-8') as f:
        while True:
            str = f.readline()
            if str == "":
                break

            if str.strip() == "":
                continue
            stu = str.strip().split(',')

            for i,v in enumerate(stu):
                if i == 0 or i == 1: continue
                elif 2<=i<=5:
                    stu[i] = int(v)
                elif i == 6:
                    stu[i] = float(v)
                elif i == 7:
                    stu[i] = int(v)

            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))
            stuNum += 1

def writeStu():
    with open("C:\\aaa\\stu.txt",'w',encoding='utf-8') as f:
        for s in stus.slist: # stus에 있는 한 줄은
            str = s.s_str() # student의 쓰기함수 양식으로 해서 str로 지정
            f.write(str+'\n')

def main_screen():
    while True:
        print("-"*70)
        print("[학생성적관리프로그램]")
        print("-"*70)
        print("[1.학생성적입력관리]")
        print("[2.학생성적출력관리]")
        print("[3.학생성적수정관리]")
        print("[9.학생성적저장관리]")
        print("[0.프로그램종료]")

        choice = input("원하는 작업 선택:")
        if not choice.isdigit():
            print("숫자를 입력하세요.")
        else:
            choice = int(choice)
        return choice

def s_input():
    global stuNum
    while True:
        print('[학생성적입력]')
        no = stuNum
        name = input("학생이름:")
        kor = int(input("국어:"))
        eng = int(input("영어:"))
        math = int(input("수학:"))
        total = kor+eng+math
        avg = total/3
        rank = 0

        stus.add(Student(no,name,kor,eng,math))
        print(f"{name}학생 성적이 입력되었습니다.")
        stuNum += 1

def s_output():
    with open("C:\\aaa\\stu.txt",'r',encoding='utf-8') as f:
        for s in stus.slist:
            str = s.s_str()
            f.write(str+'\n')


def s_update():
    temp = 0
    print("-"*70)
    print("[학생성적수정]")
    print("-"*70)
    name = input("수정할 학생:")
    for s in stus.slist:
        if s.name == name:
            print(f"{name}학생을 찾았습니다.")
            temp = 1
            print("[1.국어,2.영어,3.수학]")
            choice = int(input("수정할 과목:"))
            if choice == 1:
                print(f"현재 {name}학생 국어성적은 {s.kor}입니다.")
                s.kor = int(input("수정 국어점수:"))

            if choice == 2:
                print(f"현재 {name}학생 영어성적은 {s.eng}입니다.")
                s.eng = int(input("수정 영어점수:"))

            if choice == 3:
                print(f"현재 {name}학생 수학성적은 {s.math}입니다.")
                s.math = int(input("수정 수학점수:"))

            s.cal_total()
            s.cal_avg()
            print(f"{name}학생 성적이 수정되었습니다.")

        if temp ==0:
            print(f"{name}학생은 없습니다.")