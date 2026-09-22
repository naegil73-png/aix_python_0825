# # 
# def number_func(m_num):
#     pass

# def gugudan_func(i,j):
#     pass

# def cal_func(num1,num2):
#     pass

# while True:
#     print("1.1~10까지 숫자맞추기 프로그램")
#     print("2.구구단 출력프로그램")
#     print("3.두수를 입력받아 +,-,*,/ 결과값 출력프로그램")
#     choice = int(input("원하는 번호입력: "))

#     if choice == 1:
#         while True:
#             import random
#             count = 1
#             r_num = random.randint(1,10)
#             m_num = int(input("입력숫자:"))
#             if m_num == r_num:
#                 print("정답입니다.")
#                 break
#             elif m_num > r_num:
#                 print("보다 작은 숫자를 넣으세요.")
#             else:
#                 print("보다 큰 숫자를 넣으세요.")
#             number_func(m_num)

#     elif choice == 2:
#         for i in range(2,10):
#             for j in range(1,10):
#                 print(i,"X",j,"=",i*j)
#             print()
#         gugudan_func(i,j)

#     elif choice == 3:
#         num1 = int(input("숫자입력: "))
#         num2 = int(input("숫자입력: "))
#         print("덧셈 :", num1 + num2)
#         print("뺄셈 :", num1 - num2)
#         print("곱셈 :", num1 * num2)
#         print("나눗셈 :", num1 / num2)
#         cal_func(num1,num2)


# 함수에 적용
def number_func(m_num):
    if m_num == r_num:
        print("정답입니다..")
    elif m_num > r_num:
        print("보다 작은 숫자를 넣으세요.")
    else:
        print("보다 큰 숫자를 넣으세요.")
def gugudan_func():
    for i in range(2,10):
        for j in range(1,10):
            print(i,"X",j,"=",i*j)
        print()
def cal_func(num1,num2):
    print("덧셈 :", num1 + num2)
    print("뺄셈 :", num1 - num2)
    print("곱셈 :", num1 * num2)
    print("나눗셈 :", num1 / num2)

while True:
    print("1.1~10까지 숫자맞추기 프로그램")
    print("2.구구단 출력프로그램")
    print("3.두수를 입력받아 +,-,*,/ 결과값 출력프로그램")
    choice = int(input("원하는 번호입력: "))

    if choice == 1:
        import random
        r_num = random.randint(1,10)
        while True:
            m_num = int(input("입력숫자:"))
            number_func(m_num)
    elif choice == 2:
        gugudan_func()
    elif choice == 3:
        num1 = int(input("숫자입력: "))
        num2 = int(input("숫자입력: "))
        cal_func(num1,num2)