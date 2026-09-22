# 함수사용이유 : 긴 구문의 반복적인 명령어를 줄일 수 있음
# 코드를 간결하게 하기 위해서 함수 사용
# ******* 반복적인 작업을 함수로 선언해야 함

# 구조 : def 함수명():
# 용도 : 반복적인 구문을 줄이기 위해 사용

# def fun(): # 함수 정의시작
#     print("함수를 호출합니다.") # 함수 내용
# fun() # 함수 호출

# num1 = int(input("숫자입력: "))
# num2 = int(input("숫자입력: "))
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# # 사칙연산으로 계산 -> 함수로 할 수도 있음

# def cal():
#     num1 = int(input("숫자입력: "))
#     num2 = int(input("숫자입력: "))
#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)
# cal()

# 함수를 이용한 성적출력

def stu_print(): # 학생 성적 출력하는 함수
    for s in stu[3:]:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s)) # *s는 요소 전체를 출력하는 구문임. 일부만 넣으면 에러 발생

stu = [
    [1,"홍길동",100,100,100,300,100],
    [2,"유관순",100,100,100,300,100],
    [3,"이순신",100,100,100,300,100]
]

c_no = 0
while True:
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요.>>"))
    if choice == 1:
        print()
        while True:
            print("[학생성적입력]")
            no = c_no+1
            name = input("이름을 입력하세요(0.이전페이지 이동):")
            if name == "0": break
            kor = int(input("국어성적:"))
            eng = int(input("영어성적:"))
            math = int(input("수학성적:"))
            total = kor+eng+math
            avg = total/3
            stu.append([no,name,kor,eng,math,total,avg])
            c_no += 1
        # 학생전체출력
    elif choice == 2:
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        stu_print() # 함수를 호출한다.
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        name = input("이름을 입력하세요:")
