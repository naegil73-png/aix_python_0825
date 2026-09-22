# title = ["번호","이름","국어","영어","수학","합계","평균"] 으로 성적 입력, 출력, 수정 기능 구현

title = ["번호","이름","국어","영어","수학","합계","평균"]
stu = []
sno = 1
temp = 0


def main_screen():
    print("[학생성적관리프로그램]")
    print("[1.학생성적입력관리]")
    print("[2.학생성적출력관리]")
    print("[3.학생성적수정관리]")

def s_con():
    pass

while True:
    main_screen()

    s_con()
    choice = int(input("원하는 작업을 선택하시오:"))
    if choice == 1:
        print("[학생성적입력관리]")
        while True:
            no = sno
            name = input(f"{title[1]} 입력:")
            if name == "0":
                print("입력을 종료합니다.")
                break
            kor = int(input(f"{title[2]}성적입력 :"))
            eng = int(input(f"{title[3]}성적입력 :"))
            math = int(input(f"{title[4]}성적입력 :"))
            # for i in range(3):
            #     score = int(input(f"{title[i+2]}과목 성적 입력"))
            total = kor+eng+math
            avg = total/3
            stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
            print(name,"학생 성적이 입력되었습니다.")
            sno += 1
            
    elif choice == 2:
        print("[학생성적출력관리]")
        print("-"*60)
        print(f"{title[0]}\t{title[1]}\t{title[2]}\t{title[3]}\t{title[4]}\t{title[5]}\t{title[6]}")
        print("-"*60)
        if len(stu) ==0:
            print("입력된 자료가 없습니다.")
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
        print("-"*60)
    elif choice == 3:
        print("[학생성적수정관리]")
        name = input("찾는 학생 이름:")
        for i, s in enumerate(stu):
            if s['name'] in name:
                temp = 1
                print(f"{name}학생을 찾았습니다.")
                break
            # else:
            #     print(f"{name}학생은 없습니다.")
        if temp == 0:
            print(f"{name}학생은 없습니다.")
        else:
            sub = int(input("수정과목 입력:"))
            print("1.국어, 2.영어, 3.수학")
            if sub == 1:
                print(f"현재 {name}학생 {title[i+2]} 성적은 {s['kor']}입니다.")
                s['kor'] = int(input("수정할 성적을 입력하세요."))
                print(f"{title[i+2]}과목의 성적이 {s['kor']}로 수정되었습니다.")
            elif sub == 2:
                print(f"현재 {name}학생 {title[i+2]} 성적은 {s['eng']}입니다.")
                s['eng'] = int(input("수정할 성적을 입력하세요."))
                print(f"{title[i+2]}과목의 성적이 {s['eng']}로 수정되었습니다.")
            elif sub == 3:
                print(f"현재 {name}학생 {title[i+2]} 성적은 {s['math']}입니다.")
                s['math'] = int(input("수정할 성적을 입력하세요."))
                print(f"{title[i+2]}과목의 성적이 {s['math']}로 수정되었습니다.")

    elif choice == 4:
        print("[학생성적수정관리]")
        name1 = input("삭제하실 학생 이름:")
        for i, s in enumerate(stu):
            if s['name'] in name1:
                print(f"{name1}학생을 찾았습니다.")
                temp = 1
            else:
                print(f"{name1}학생은 없습니다.")
