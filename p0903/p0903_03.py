def cal1():
    for i in range(2,10):
        for j in range(1,10):
            print("{} X {} = {}".format(i,j,i*j))

def cal2(num1,num2):

    print("덧셈:", num1+num2)
    print("뺄셈:", num1-num2)
    print("곱셈:", num1*num2)
    print("나눗셈:", num1/num2)

def cal3():
    total = 0
    for i in range(1,11):
        total += i
    print(total)

while True:
    print("1.구구단 출력")
    print("2.두수를 입력받아 +, -값을 출력")
    print("3.1~10까지 합을 출력")
    print("그만하려면, 0을 입력")
    choice = int(input("원하는 번호를 입력하세요:"))

    if choice == 1:
        cal1()
    elif choice == 2:
        num1 = int(input("숫자입력:"))
        num2 = int(input("숫자입력:"))
        cal2(num1,num2)
    elif choice == 3:
        cal3()

    elif choice ==0:
        print("프로그램 종료")

# 가변 매개변수 : 함수의 변수 갯수가 변할 경우, 자동적으로 입력하는 변수 갯수를 조정하는 변수 -> *