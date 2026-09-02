# 반복하는 횟수가 있을 때는 for, 조건식이 있을 때는 while

for i in range(1,11):
    print(i)


#위의 내용을 while문으로 같은 결과를 출력

# while문은 조건식이 만족하는 한 반복
i = 1
while i < 11:
    print(i)
    i += 1

for i in range(1,11,2):
    print(i)

i = 1
while i<11:
    print(i)
    i += 2

# 모든 for문은 while변경 가능함
# for : 반복, 구간지정 1-10까지 등 지정이 있을 때
# while : 조건식이 있을 때 주로 사용, 무한반복일 때 사용

# # 무한반복 구간
# i = 0
# while True:
#     print(i)
#     i += 1

# **** while문은 초기값, 조건식, 증감식이 반드시 있어야 함
# while문을 이용해서 alist에 있는 값을 출력
alist = list(range(10)) # alist = [0,1,2....,9]

i = 0
while i<10: # alist의 원소 갯수
    print(alist[i], end =" ")
    i += 1
print()


# alist = ["바나나","딸기","수박"]
# # alist 안에 있는 원소를 하나씩 출력
# # 0:바나나
# # 1:딸기
# # 2:수박  으로 출력

# i = 0
# while i<3: # 또는 i < len(alist)해도 됨
#     print("{}:{}".format(i, alist[i]))
#     i += 1

# for i in alist:
#     print("{}:{}".format(i, alist[i])) # while문보다 짧음 -> 반복식은 for문이 유리.

# # while문 무한루프
# i = 0
# while True:
#     print(i)

# # 만약, 10의 배수일 때, 프로그램을 종료할까요를 표시하는 명령문
# i = 0
# while True:
#     print(i)
#     if i%10 ==0:
#         input1 = input("프로그램을 종료할까요?")
#         if input1 == "x":
#             break
#     i += 1
# print("프로그램 종료")

# 두수를 입력받아 합을 구하는 무한반복 프로그램을 구현하시오. 단, 입력 수 중 0이 있으면, 종료되게 구현하시오.
# while문 밖에 작성하면, 입력 한번으로 무한 루프, 안에 넣으면 계속 입력해야 함

while True:
    num1 = int(input("숫자1:"))
    num2 = int(input("숫자2:"))
    sum = num1+num2
    print("{} + {} = {}".format(num1,num2,sum))
    if num1==0 or num2==0:
        print("종료합니다.")
        break

