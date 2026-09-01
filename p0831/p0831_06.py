ranNo = [1,5,9,7,4]
inputNo = [1,2,3,4,5]

# 입력한 숫자와 랜덤숫자가 몇 개 맞는 지 갯수를 출력

num = 0
for i in inputNo:
    if i in ranNo:
        num += 1
    else: continue
print("개수:",num)

# 일치하는 숫자도 출력하려면..
num = 0
answerNo = []
for i in inputNo:
    if i in ranNo:
        num += 1
        answerNo.append(i)
    else: continue
print("개수:",num, answerNo)

# 맞출 때까지 입력하는 프로그램
# 입력한 숫자를 모두 저장해서 프로그램을 종료할 때 출력하시오.
# 0을 입력시 프로그램 종료. noArr 값과 일치하는 갯수 출력

'''
noArr = [10,40,2,9,5]
no = []
answer = []
count = 0
while True:
    i_no = int(input("숫자입력:"))
    if i_no == 0: # 0을 입력할 때 종료
        break
    no.append(i_no) # 0은 출력하지 않아도 되므로 0은 추가에서 제외하기 위해 추가 구문에서 제외
print("입력한 숫자들:",no)
for i in no:
    if i in noArr:
        count += 1
        answer.append(i)
    else: continue
print("맞춘 갯수:", count)
print("정답숫자", answer)
'''

# lotto 프로그램 만들기

import random
alist = list(range(1,46))
random.shuffle(alist) # 리스트를 섞어줌
print(alist)

'''
# 랜덤으로 개수만큼 추출(중복이 안됨)
ranArr = random.sample(1,46,6) # sample(range(1,46),6) 이렇게 해도 됨
print(ranArr)

# 랜덤으로 개수만큼 추출(중복가능)
ranArr2 = random.choices(range(1,46),k=6)
print(ranArr2)
'''
'''
# 입력한 숫자 1개가 맞는 지 출력
import random
lotto = random.sample(range(1,46),6)
print("로또번호 :",lotto)

mynum = int(input("숫자입력:"))
if mynum in lotto:
    print("있습니다.")
else:
    print("꽝")

# 6개 입력받아 있는 지 확인하시오.
# 로또번호 : 
# 정답번호 :
# 정답개수 :
'''

import random
lotto = random.sample(range(1,46),6)
i = 0
mynum = []
while i < 6:
    mynum1 = int(input("숫자입력"))
    if mynum1 not in mynum:
        mynum.append(mynum1)
        i = i+1
    else:
        print("숫자가 있습니다. 다른 숫자를 고르세요")
answer = []
count = 0
for i in mynum:
    if i in lotto:
        count += 1
        answer.append(i)
print("로또번호:",lotto)
print("선택번호:",mynum)
print("정답번호:",answer)
print("정답개수:",count)

# 숫자범위를 잘못 넣었을 때

import random
lotto = random.sample(range(1,46),6)
i = 0
mynum = []
while i < 6:
    mynum1 = int(input("숫자입력"))
    if mynum1 not in mynum:
        i = i+1
    else:
        print("숫자가 있습니다. 다른 숫자를 고르세요") # 잘못 입력했을 때, 횟수가 추가되지 않게 하기 위해 i = i+1 하지 않음
    if mynum1 < 1 or mynum1 > 45:
        print("1~45사이 숫자로 골라주세요.")
    else:
        mynum.append(mynum1)

answer = []
count = 0
for i in mynum:
    if i in lotto:
        count += 1
        answer.append(i)
print("로또번호:",lotto)
print("선택번호:",mynum)
print("정답번호:",answer)
print("정답개수:",count)

