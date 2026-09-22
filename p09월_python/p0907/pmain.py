stuList = []
title = ['번호','이름','국어','영어','수학','합계','평균','순위']
s_title = ['no','name','kor','eng','math','total','avg','rank']
stuNum = 1
rank = 0

with open("C:\\aaa\\stu.txt",'r',encoding='utf-8') as f:
    while True:
        str = f.readline()
        print(str)
        if str == "": break
        str = str.strip()
        stu = str.split(",")
        for i, v in enumerate(stu):
            if i ==0 or i == 1:continue
            elif 2<= i <= 5:
                stu[i] = int(v.strip())
            elif i == 6:
                stu[i] = float(v.strip())
        stuList.append(dict(zip(s_title,stu)))
        stuNum = len(stuList)+1
        

while True:
    print('[학생성적관리프로그램]')
    print("-"*60)
    print('[학생성적입력관리]')
    print('[학생성적출력관리]')
    print('[학생성적수정관리]')

    choice = input("원하는 작업 선택(1~3):")
    if choice.isdigit():
        choice = int(choice)
        pass
    else:print("숫자를 입력하세요.")

    if choice == 1:
        while True:
            print('[학생성적입력]')
            print("-"*60)
            no = stuNum
            name = input("학생이름:")
            if name == "0": break
            kor = int(input("국어:"))
            eng = int(input("영어:"))
            math = int(input("수학:"))
            total = kor+eng+math
            avg = total/3
            stuList.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
            stuNum += 1
            print(f"{name}학생 성적이 입력되었습니다.")

    elif choice == 2:
        print("-"*60)
        print('[학생성적출력]')
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        if len(stuList) == 0:
            print("입력된 학생이 없습니다.")
        for i in stuList:
            print(f"{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']}\t{i['rank']}")
