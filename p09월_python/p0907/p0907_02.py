# # 두수를 입력받아 두수의 합을 구하시오. -> 3가지 방법

# # 함수 표현식
# def hap():
#     num1 = int(input("숫자입력1:"))
#     num2 = int(input("숫자입력2:"))
#     sum = num1+num2
#     print(sum)

# hap()

# # *** 아랫구문으로 출력하려면, 결과값을 아래로 전달해야 하므로 return명령어가 있어야 함 ***
# def hap():
#     num1 = int(input("숫자입력1:"))
#     num2 = int(input("숫자입력2:"))
#     sum = num1+num2
#     return sum

# sum = hap()
# print(sum)

# # 입력을 호출문에서 하려면, 함수에 변수를 지정해야 함

# def hap(num1,num2):
#     sum = num1+num2
#     return sum

# num1 = int(input("숫자입력1:"))
# num2 = int(input("숫자입력2:"))
# sum = hap(num1,num2)
# print(sum)

# # 위의 함수표현식에서
# # 첫번째는 매개변수X,return X
# # 두번째는 매개변수X,return o
# # 세번째는 매개변수o,return o

# def hap2():
#     num1 = int(input("숫자입력:"))
#     num2 = int(input("숫자입력:"))
#     sum = num1+num2
#     print(sum)

#     hap2()

# def hap3():
#     num1 = int(input("숫자입력:"))
#     num2 = int(input("숫자입력:"))
#     sum = num1+num2
#     return sum

# sum = hap2()
# print(sum)


# def hap4(num1,num2):
#     sum = num1+num2

#     return sum

# for i in range(10):
#     num1 = int(input("숫자입력3:"))
#     num2 = int(input("숫자입력4:"))
#     sum = hap4(num1,num2)
# print(sum)

import func
func.hap2()
sum = func.hap3()
print(sum)

num1 = int(input("숫자입력3:"))
num2 = int(input("숫자입력4:"))
sum = func.hap4(num1,num2)
print(sum)

'''
import func as fn # 별칭으로 명명가능 # fn.hap2()
from func import hap2,hap3,hap4 # -> func.hap2는 안써도 됨. hap2만 써도 됨
'''

