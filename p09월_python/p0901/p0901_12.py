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
while True: # 선택메뉴는 항상 보이게 처리
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

    choice = int(input("숫자를 입력하세요:")) # 하단에 메뉴선택 입력 기능 추가
    if choice == 1: # 학생성적 입력을 선택하면, 사용자가 중단할 때까지 입력하도록 기능 추가
        print("[학생성적 입력]")
        while True: 
            no = len(stu_list)+1 # len(1)은 0부터 1직전까지 이므로 0만 반환 -> 따라서 +1이 필요
            print("번호",no)
            name = input("이름 입력:")
            if name == "0": break # 입력을 중단한다는 구문
            kor = int(input("국어:")) # 이후는 학생의 입력항목
            eng = int(input("영어:"))
            math = int(input("수학:"))
            total = kor+eng+math
            avg = total/3
            stu_list.append([no,name,kor,eng,math,total,avg]) # 입력항목 추가
            print(name," 학생 성적이 등록되었습니다.") # 입력항목 추가 결과 표시
    elif choice == 2:
        print("[학생성적 출력]")
        print("입력된 학생 성적:", len(stu_list)) # 입력된 학생 수 출력
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*50)
        for i in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*i)) # 학생의 입력항목을 출력, *i는 stu_list에 있는 요소를 분리해서 각각 적용해 줌

    elif choice == 3:
        print(choice,"학생성적수정")
    elif choice == 4:
        print(choice,"학생성적삭제")
    elif choice == 5:
        print(choice,"학생검색")
    elif choice == 6:
        print(choice,"학생이름정렬")
    elif choice == 7:
        print(choice,"학생합계정렬")
    elif choice == 0:
        print(choice,"프로그램을 종료합니다.")
        break