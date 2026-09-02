# # 입력한 숫자가 양수인지, 음수인지 출력하시오
# # 절차 : 1.숫자입력, 2.양수, 음수 비교, 3. 출력

# a = int(input("숫자입력 : "))
# if a > 0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")
# print("입력숫자 :", a)

# # 입력한 숫자가 2의 배수인지, 아닌지 출력하시오.

# a = int(input("숫자입력 : "))
# if a%2==0: 
#     print("2의 배수입니다.")
# else:
#     print("2의 배수가 아닙니다")
# print("입력숫자 :",a)

# # 비교연산자 : ==, !=, >,<,>=,<= 
# # 산술연산자 : +,-,*,/,//,%,**
# # 논리연산자 : and, or, xor

# 랜덤함수(임의의 숫자를 뽑아주는 함수)
import random # 파이썬에 있는 random클래스를 사용하겠다고 선언하는 것

num = random.randint(1,100) # randint(임의의 정수(int))를 1~100까지 정수 중 임의로 1개 수를 반환함(random클래스에서 임의의 정수를 뽑아라. 1~100사이)
print(num)

# 1~5 랜덤 숫자를 출력하시오.
import random
num = random.randint(1,5)
input1 = int(input("1~5까지 범위의 숫자를 입력하세요: "))
input2 = int(input("1~5까지 범위의 숫자를 입력하세요: "))
print('랜덤숫자:',num)
print('입력숫자:',input1, input2)
if (num==input1) or (num==input2):
    print("당첨되셨습니다.")
else:
    print("꽝, 다음 기회에")