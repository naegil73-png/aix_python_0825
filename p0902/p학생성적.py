# # 학생성적 : 이 구문 반드시 암기할 것
# stu = [
#     {"no:1","name":"홍길동","kor":100, "eng":100,"math":100},
#     ]

# 화면 출력
# 1. 성적입력
# 2. 성적출력

c_no = 0 # 학생번호로 사용
stu = []
while True:
    # 메인화면 출력부분
    print("[학생성적프로그램]")
    print("-"*60)
    print("1: 학생성적입력")
    print("2: 학생성적출력")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요."))
    
    # 학생성적 입력부분
    if choice == 1:
        print()
        print("[학생성적입력]")
        while True:
            no = c_no + 1
            name = input("학생이름입력: ")
            if name == "0": break
            kor = int(input("국어점수입력:"))
            eng = int(input("영어점수입력:"))
            math = int(input("수학점수입력"))
            total = kor+eng+math
            avg = total/3
            stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
            print(name,"학생 성적이 입력되었습니다.")
            c_no += 1 # 다음번호
            print()

    # 학생성적 출력부분    
    elif choice == 2:
        print()
        print("[학생성적출력]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        # 딕셔너리는 하나하나 입력해줘야 함(*s같이 축약 불가)
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}") # 딕셔너리는 *s형태로 입력 불가
        print()

