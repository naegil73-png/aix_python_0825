## 학생성적을 구조화 : 입력사항은 no, name, kor, eng, math, total, avg임. 이름에 0을 입력하면 입력이 종료
# # 이제까지는 입력 후 출력
# print("[학생성적프로그램]")
# print("1. 학생입력")
# print("2. 학생출력")
# print("3. 학생성적수정")
# print("4. 학생성적삭제")
# print("5. 학생검색")
# print("6. 학생이름정렬")
# print("7. 학생합계정렬")
# print("0. 프로그램 종료")
# print("-"*40)

stu_list = []
while True:
    print("[학생성적프로그램]")
    print("1. 학생입력")
    print("2. 학생출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생검색")
    print("6. 학생이름정렬")
    print("7. 학생합계정렬")
    print("0. 프로그램 종료")
    print("-"*40)

    work = int(input("숫자를 입력하세요:"))
    if work == 1:
        print("[학생성적 입력]")
        while True:
            no = len(stu_list)+1
            print("번호",no)
            name = input("이름 입력:")
            if name == "0": break
            kor = int(input("국어:"))
            eng = int(input("영어:"))
            math = int(input("수학:"))
            total = kor+eng+math
            avg = total/3
            stu_list.append([no,name,kor,eng,math,total,avg])
            print(name," 학생 성적이 등록되었습니다.")
            print()

    elif work == 2:
        print("[학생성적 출력]")
        print("입력된 학생 성적:", len(stu_list))
        print("-"*50)
        for i in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*i))
    elif work == 3:
        pass
    elif work == 4:
        pass
    elif work == 5:
        pass
    elif work == 6:
        pass
    elif work == 7:
        pass
    elif work == 0:
        print(work,"프로그램을 종료합니다.")