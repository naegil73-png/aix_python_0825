# 함수로 1.컴퓨터 1000000, 2.세탁기 2000000, 3.오디오 500000 을 항상 표출, 입력은 제품번호/수량 형태로 하고, 제품 선택 시 선택사항과 총 구매금액을 출력
# 1/3 : 1번 3개 구매함을 의미
# 총 구매금액을 출력하시오.

# while True:
#     print("1.컴퓨터 - 1_000_000") # 이렇게 해도 숫자로 입력함
#     print("2.세탁기 - 2_000_000") # 이렇게 해도 숫자로 입력함
#     print("3.오디오 - 500_000") # 이렇게 해도 숫자로 입력함
#     choice = input("원하는 번호와 개수 입력(1/3)")
#     choice1 = choice.split("/") # split, count 등은 문자열만 가능
#     if choice1[0] == "1":
#         print("세탁기", choice1[1],"대")
#         total = int(choice1[1]) * 1000000 # 위에서 choice2 = [int(i) for i in choice1]으로 한꺼번에 변경가능
#         print("총 구매금액:",total,"원")

#     elif choice1[0] == "2": 
#         print("세탁기", choice1[1],"대")
#         total = int(choice1[1]) * 2000000
#         print("총 구매금액:",total,"원")
        
#     elif choice1[0] == "3":
#         print("오디오", choice1[1],"대")
#         total = int(choice1[1]) * 3000000
#         print("총 구매금액:",total,"원")
        
#     else:
#         print("잘못 입력하셨습니다. 1~3의 숫자를 입력하세요.")
    

#     # print(1+1+1_000_000) # 1,000,000으로 넣으면 에러가 남(각각의 원소라고 생각하기 때문에 에러가 남)
#     # 문자열 이동은 alt, 방향키

# # 두 숫자를 n1/n2 형태로 입력하고, 앞 자리 숫자에는 10, 뒷 자리 숫자에는 100을 곱한 후 합계를 구할 것
# num = input("숫자입력(1/3)") # 이런 형태로 입력
# # 앞 숫자에는 10 곱하고, 뒷 숫자에는 100을 곱해서
# # 합계를 구하시오
# # 1*10+3*100 = 310이 출력되도록 할 것

# num1 = num.split("/")
# print(int(num1[0])*10 + int(num1[1])*100)

# # ******* 한꺼번에 숫자로 변환
# num2 = [int(i) for i in num1]
# print(type(num2[0]))

# ****** 웹에서 회원가입, 은행 비밀번호 등은 모두 문자열로 받음 -> int로 변환해야 함(금액 등)


# 1.냉장고,2.세탁기,3.오디오
# 위의 구매구문을 함수로 작성

def cal(choice):
    choice1 = choice.split("/") # split, count 등은 문자열만 가능
    if choice1[0] == "1":
        print("냉장고", choice1[1],"대")
        total = int(choice1[1]) * 1000000 # 위에서 choice2 = [int(i) for i in choice1]으로 한꺼번에 변경가능
        print("총 구매금액:",total,"원")

    elif choice1[0] == "2": 
        print("세탁기", choice1[1],"대")
        total = int(choice1[1]) * 2000000
        print("총 구매금액:",total,"원")
        
    elif choice1[0] == "3":
        print("오디오", choice1[1],"대")
        total = int(choice1[1]) * 500000
        print("총 구매금액:",total,"원")
        
    else:
        print("잘못 입력하셨습니다. 1~3의 숫자를 입력하세요.")

# 프로그램 시작 ---------------------------------------------------
while True:
    print("1.컴퓨터 - 1_000_000") # 이렇게 해도 숫자로 입력함
    print("2.세탁기 - 2_000_000") # 이렇게 해도 숫자로 입력함
    print("3.오디오 - 500_000") # 이렇게 해도 숫자로 입력함
    choice = input("원하는 번호와 개수 입력(1/3)")
    # 함수호출
    cal(choice)

# 작성: def 선언구문, pass로 처리, while문 등 처리함수 내용 작성 -> def구문으로 이동, 실행문에서 함수 호출
