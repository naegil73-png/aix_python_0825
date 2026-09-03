# def func1():
#     global a # 전역변수에 선언되어 있는 링크를 가져옴 -> 같은 이름의 전역변수의 값을 가져옴 -> 간혹, 가져와야할 경우가 있음. 아니면, 매개변수를 써야 함
#     a = 10 # 지역변수 : 함수 내 있는 변수
#     print("func1 a :",a)

# def func2():
#     print("func2 a :",a)

# # 전역변수 : 함수 밖에 있는 변수
# a = 20

# func1() # func1을 찾아서 실행 -> 함수 내의 a, 10을 출력
# func2() # func2에서 함수 내 지역변수가 없음 -> 전역변수를 찾음 -> 전역변수 출력

# # 변수는 지역변수가 있는 지 찾고, 없으면 전역변수를 찾아서 출력함. 다른 함수 내의 변수는 찾을 수 없음
# # 연계된 변수 찾기 : 변수에 커서 두고 F12를 누르면 나타남..

# def func1():
#     a = 10
#     print("func1 a:",a)
# # 호출 않으면 결과없음
# func1() # 함수는 호출되면, 결과값을 반환하고 함수 내의 입력값, 명령들을 모두 삭제함

# a = 20

# print("전역변수:",a)


# def func1(a, b,c): # 매개변수이면서 지역변수
#     print(a)
#     return a+10

# c = 30 # 전역변수
# result = func1(10, 2, c) # 변수를 통한 호출 -> 식에서 사용되지 않더라도, 매개변수의 수는 일치시켜줘야 함
# print(result) 

def func1(*num):
    sum = 0
    for n in num:
        sum += n
    return sum

print(func1(1,2,3))
print(func1(1,2))
print(func1(10,20,30,40,50))

# # 2~10까지 몇개를 매개변수로 사용하든지 합계를 구하도록 para_func()함수 구하기

# def para_func(a,b,*n): # 2개 이상이어야 하므로
#     total = 0
#     for i in n:
#         total += i
#     return total

# print(para_func(2,3,4,5,6,7,8,9))

import func # func.py에서 불러온다.
func.cal1() # func.py에서 cal1함수 호출
func.cal2()
func.cal3()

from func import cal2 # 두개 이상 부르려면, cal2, cal3 등으로 해도 되고, 전부 다 부르려면 *
cal2()

from func import * # 민감 정보 때문에 *는 잘 하지 않음. import func도 정보보호 문제는 마찬가지임
func.cal1() 
func.cal2()
func.cal3()

# import 시 축약해서 가져올 수 있음
import math as m # math를 m으로 축약해서 사용
m.sin(1)

import datetime
now1 = datetime.datetime.now()
print(now1.hour)


a = max(1,2,3)
print(a)

import sys
print(sys.builtin_module_names) # 시스템에서 사용할 수 있는 함수들을 보여줌

import math
print(dir(math))
print(math.sin(10))

# ***** 버림, 반올림, 올림은 기억해 둘 것
print(math.floor(10.921)) # 버림 
print(math.ceil(10.111)) # 올림
print(round(10.111)) # 반올림
print(round(10.111,1)) # 반올림 - 소수점 첫째자리에서 반올림

