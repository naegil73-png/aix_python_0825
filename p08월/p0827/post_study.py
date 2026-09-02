'''
num = int(input("숫자 입력:"))
if num > 100:
    print("100보다 큽니다")
else:
    print("100보다 작습니다")
'''

'''
a = int(input("숫자입력: "))
b = int(input("숫자입력: "))
c = a+b
if c > 100:
    print("100보다 큽니다")
else:
    print("100보다 작습니다")
'''
    
import random
num = random.randint(1,100)

if num%2 ==0:
    print(num,"짝수입니다.")
else:
    print(num,"홀수입니다")

# 지금 계절을 표시(봄 3~5, 여름 6~8, 가을 9~11, 겨울 12~2)
import datetime
dt = datetime.datetime.now()
month = dt.month

if 3<=month<6:
    print("봄")
elif 6<=month<9:
    print("여름")
elif 9<=month<12:
    print("가을")
else:
    print("겨울")
print("{:02d}월".format(month))

import random
score = random.randint(0,100)

if score >= 90:
    if score >= 98:
        print("A+")
    elif score >= 93:
        print("A")
    else:
        print("A-")
elif score >= 80:
    if score >= 88:
        print("B+")
    elif score >= 83:
        print("B")
    else:
        print("B-")
elif score >= 70:
    if score >= 78:
        print("C+")
    elif score >= 73:
        print("C")
    else:
        print("c-")
elif score >= 60:
    if score >= 68:
        print("D+")
    elif score >= 63:
        print("D")
    else:
        print("d-")
else:
    print("F")
print("획득점수 :", score)

import random
score = random.randint(0,100)

if score >= 60:
    print("시험통과")
elif score >= 50:
    print("재시험")
else:
    print("불합격")
print("점수:",score)

arr = [1,2,3,4,5]
print(arr[2]+1)
print(len(arr))

if 1 in arr:
    print("있습니다.")
else:
    print("없습니다.")

# 로또번호 
import random
lotto = random.sample(range(1,46),6)
lotto_final = sorted(lotto[:-1])+lotto[-1:]

choice_num = []
choice_num.append(int(input("1번째 숫자:")))
choice_num.append(int(input("2번째 숫자:")))
choice_num.append(int(input("3번째 숫자:")))
choice_num.append(int(input("4번째 숫자:")))
choice_num.append(int(input("5번째 숫자:")))
choice_num.append(int(input("보너스 숫자:")))

match = 0
if choice_num[0] in lotto:
    match += 1
if choice_num[1] in lotto:
    match += 1
if choice_num[2] in lotto:
    match += 1
if choice_num[3] in lotto:
    match += 1
if choice_num[4] in lotto:
    match += 1
if choice_num[5] in lotto:
    match += 1

if match == 6:
    print("축하드립니다. 1등에 당첨되셨습니다.")
if match == 5:
    print("축하드립니다. 2등에 당첨되셨습니다.")
if match == 4:
    print("아쉽지만, 3등에 당첨되셨습니다.")
if match == 3:
    print("그냥 일이나 하세요. 4등에 당첨되셨습니다.")
if match <= 2:
    print("야, 자동선택해. 아니면, 로또는 꿈도 꾸지마!!")
print("lotto 당첨번호는",lotto)
print("lotto 당첨번호는",lotto_final)
print(match,"개 맞췄습니다.")

# lotto 자동선택

import random
lotto = random.sample(range(1,46),6)
lotto_final = sorted(lotto[:-1])+lotto[-1:] # 당첨번호 정렬, 단, 보너스번호는 정렬 제외

choice_num =random.sample(range(1,46),6)

match = 0
if choice_num[0] in lotto:
    match += 1
if choice_num[1] in lotto:
    match += 1
if choice_num[2] in lotto:
    match += 1
if choice_num[3] in lotto:
    match += 1
if choice_num[4] in lotto:
    match += 1
if choice_num[5] in lotto:
    match += 1

if match == 6:
    print("축하드립니다. 1등에 당첨되셨습니다.")
if match == 5:
    print("축하드립니다. 2등에 당첨되셨습니다.")
if match == 4:
    print("아쉽지만, 3등에 당첨되셨습니다.")
if match == 3:
    print("그냥 일이나 하세요. 4등에 당첨되셨습니다.")
if match <= 2:
    print("로또는 꿈도 꾸지마!!")
print("자동선택 lotto 당첨번호는",lotto)
print("lotto 당첨번호는",lotto_final)
print(match,"개 맞췄습니다.")