# # 1~5까지 출력되는 함수

# def print1():
#     print(1,end = " ")
#     print(2,end = " ")
#     print(3,end = " ")
#     print(4,end = " ")
#     print(5)

# print1()

# while True:
#     num1 = int(input("숫자입력:"))
#     print1()

# # 매개변수로 값을 전달하는 함수

# def print1(n):
#     for i in range(n): # 입력한 수 만큼 반복
#         print("안녕하세요.")


# while True:
#     num1 = int(input("숫자입력:"))
#     print1(num1)

# # ******** 함수는 호출하는 문장 위에 있어야 함. 
# # 이유 : 함수를 호출을 하면서 함수를 실행해야 하는 데, 호출이 위에 있으면, 함수가 정의되지 않은 상태여서 실행되기 때문에 오류가 발생함

# def print1(n,s):
#     for i in range(n): # 입력한 수 만큼 반복
#         print(i+1,s)


# while True:
#     num1 = int(input("숫자입력:"))
#     str1 = input("출력하려는 문구를 입력: ")
#     print1(num1, str1) # 함수호출 문의 변수 갯수는 함수 정의 구문의 매개변수 수가 같아야 함

# 함수리턴
def add(num1,num2):
    sum = num1+num2
    return sum # return은 호출하는 곳으로 값을

while True:
    num1 = int(input("숫자입력: "))
    num2 = int(input("숫자입력: "))
    total = add(num1,num2) 
    print("결과값:",total)

# 수식을 활용하고 싶으면 함수 호출, 계산된 값을 호출한 곳으로 전달하고 싶으면 return을 써야 함.
# 함수를 직접, add(num1,num2)로 호출하는 게 아니라, total = add(num1,num2)와 같이 호출하면 return을 써야 함