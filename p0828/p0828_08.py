# 날짜함수, 랜덤함수
import datetime

today = datetime.datetime.now()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

import random
r_num = random.randint(1,12)
# 3,4,5 봄, 6,7,8 여름, 9,10,11 가을 12,1,2

if 3<=r_num<6:
    print("봄")
elif 6<=r_num<9:
    print("여름")
elif 9<=r_num<12:
    print("가을")
else:
    print("겨울")
print(r_num,"월")

# now.month
# 01월, 02월

# 랜덤 5개 뽑아내는 방법
import random
a = random.randint(1,45)
alist1 = [0,0,0,0,0]
alist2 = [0]*5
alist3 = list(range(1,6)) # for문, 반복문에 주로 사용
print(alist1)
print(alist2)
print(alist3)

arr = random.sample(range(1,46),5) # 1~45까지 중복없이 5개를 가져옴
print(arr)

arr2 = random.sample([1,2,3,4,5],2)
print(arr2)

arr3 = random.shuffle([1,2,3,4,5]) # shuffle은 대상자료를 섞어주는 역할

a1 = [1,2,3,4,5]
random.shuffle(a1)
print(a1)

arr4 = [1,2,3,4,5]
arr5 = random.choices(arr4,k=5) # choice는 리스트에서 해당갯수만큼 가져옴. 중복 가능
print(arr5)

# 1~45까지 랜덤5개를 가져와서 입력한 숫자가 있으면 당첨, 없으면 꽝
# 입력은 1개 우선해 보고, 5개

'''
# 1개 숫자
import random
lotto = random.sample(range(1,46),5)

num = int(input("숫자입력:"))
if num in lotto:
    print("당첨")
else:
    print("꽝")
print("lotto번호",lotto)

# 5개 숫자

import random
lotto = random.sample(range(1,46),5)

num1 = int(input("숫자1 입력:"))
num2 = int(input("숫자2 입력:"))
num3 = int(input("숫자3 입력:"))
num4 = int(input("숫자4 입력:"))
num5 = int(input("숫자5 입력:"))

if num1 in lotto:
    print("당첨")
elif num2 in lotto:
    print("당첨")
elif num3 in lotto:
    print("당첨")
elif num4 in lotto:
    print("당첨")
elif num5 in lotto:
    print("당첨")
else:
    print("꽝")
print("lotto번호",lotto)

# list로 작성
import random
lotto = random.sample(range(1,46),5)
num = []
num.append(int(input("숫자1 입력:")))
num.append(int(input("숫자2 입력:")))
num.append(int(input("숫자3 입력:")))
num.append(int(input("숫자4 입력:")))
num.append(int(input("숫자5 입력:")))

if num[0] in lotto:
    print("당첨")
elif num[1] in lotto:
    print("당첨")
elif num[2] in lotto:
    print("당첨")
elif num[3] in lotto:
    print("당첨")
elif num[4] in lotto:
    print("당첨")
else:
    print("꽝")
print("lotto번호",lotto)

# 경우마다 명령구문을 작성 -> 복잡, 번거로움 -> 반복문 필요
# for 문
'''
'''
import random
lotto = random.sample(range(1,46),5)
iarr = []
for i in range(5):
    iarr.append...
'''

# 리스트값 변경
a = [1,2,3,4,5]
a[2]=30
print(a)
a.pop(2)
print(a)
a.append(200)
print(a)