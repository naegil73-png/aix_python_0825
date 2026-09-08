# 학생 성적 관리프로그램을 개발
# 성적조회는 '번호','이름','국어','영어','수학','합계','평균','순위'로 표시하고,
# 프로그램은 입력, 출력, 수정, 삭제 기능으로 표시. 함수로 구현하고, 실행은 다른 pfunc.py에서 함

# 제작 사고 : 구현틀 - 입력, 조회, 수정, 삭제 항상 표출 -> 조회 -> stu, 조회내용 -> '번호','이름','국어','영어','수학','합계','평균','순위'
# 입력은 중단할 때까지 지속, while True, 과목 성적관련은 숫자, 출력은 입력 내용이 있을 때 위의 내용으로 출력
# 수정은 대상학생 조회, 과목성적을 지정, 합계, 평균도 변경

stuList = []
title = ['번호','이름','국어','영어','수학','총점','평균','등수']
s_title = ['no','name','kor','eng','math','total','avg','rank']

def readstu():
    with open("C:\\aaa\\stu.txt",'r',encoding='utf-8') as f:
        while True:
            str = f.readline()
            if str == "": break
            str = str.strip()
            stu = str.split(",")

            for i,v in enumerate(stu):
                if i == 0 or i == 2: continue
                elif 2<= i <= 5:
                    stu[i] = int(v)
                elif i == 6:
                    stu[i] = float(v)
            stuList.append(dict(zip(s_title,stu)))

def main_screen():
    while True:
        print("-"*60)
        print("[학생성적관리프로그램]")
        print("-"*60)
        print("[1.학생성적입력관리]")
        print("[2.학생성적출력관리]")
        print("[3.학생성적수정관리]")
        print("[4.학생성적삭제관리]")
        print("-"*60)

        choice = input("원하는 작업(1~4 중 하나를 고르시오):")
        if choice.isdigit():
            choice = int(choice)
            if choice > 4 or choice <1:
                print("1~4사이의 숫자를 입력하세요.")
            else:
                pass
        else:
            print("숫자를 입력하세요.")
        return choice

def s_input():
    while True:
        print("[학생성적입력]")
        no = len(stuList)+1
        name = input("학생이름(0:이전메뉴):")
        if name == "0": break
        kor = int(input("국어성적:"))
        eng = int(input("영어성적:"))
        math = int(input("수학성적:"))
        total = kor+eng+math
        avg = total/3
        rank = 0
        stuList.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{name}학생의 성적이 입력되었습니다.")

def s_output():
        print("-"*60)
        print("[학생성적조회관리]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
        print("-"*60)
        if len(stuList) == 0:
            print("입력된 학생이 없습니다.")
            return
        for i in stuList:
            print(f"{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']}\t{i['rank']}")

def s_modi():
    print("-"*60)
    print("학생성적수정관리")
    print("-"*60)
    m_s = input("수정할 학생이름:")
    if 