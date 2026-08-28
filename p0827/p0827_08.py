# 1.1~100까지 랜덤숫자 3개를 리스트에 추가해서 
# 2.입력한 숫자 1개가 있는지를 확인해서
# 3.있으면 당첨, 없으면 꽝
# 4.랜덤숫자 리스트 출력
# 5.입력숫자 출력

'''
import random

num_list = []
num = random.randint(1,100)
no1 = int(input("1.입력숫자:"))
no2 = int(input("2.입력숫자:"))
no3 = int(input("3.입력숫자:"))

num_list.append(no1)
num_list.append(no2)
num_list.append(no3)

if num in num_list:
    print("당첨")
else:
    print("꽝")
print("랜덤숫자:",num)
print("입력숫자:",num_list)
'''

import random

num_list = []
num1 = random.randint(1,100)
num2 = random.randint(1,100)
num3 = random.randint(1,100)
no = int(input("입력숫자:"))

num_list.append(num1)
num_list.append(num2)
num_list.append(num3)

if no in num_list:
    print("당첨")
else:
    print("꽝")
print("랜덤숫자:",num_list)
print("입력숫자:",no)

# 중복되지 않고 1~100사이 값을 중복 추출하려면..
import random
num_list=[]
arr2 = random.sample(range(1,101),3) # 1~100까지 범위의 수에서 3개를 중복없이 뽑아라
no = int(input("입력숫자:"))
arr2.sort()
num_list.append(arr2)

if no in num_list:
    print("당첨")
else:
    print("꽝")
print("랜덤숫자:",num_list)
print("입력숫자:",no)