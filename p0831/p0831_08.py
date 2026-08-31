# *********** 랜덤번호 맞추기, 로또번호 맞추기는 반드시 외울 것

# 1~100사이의 랜덤번호를 맞추는 프로그램을 구현 
# 랜덤번호보다 높은 수를 입력하면 낮은 숫자입력, 낮으면 높은 숫자 입력 멘트 출력
# 정답을 맞추면
# 정답숫자 : 
# 숫자입력 횟수 :
# 입력한 숫자 :

# 순서 : import random, input 함수, if문 일치여부, 입력횟수 len, my_num변수

import random
num = random.randint(1,101)
num_list = []
count = 0
while True:
    my_num = int(input("입력숫자:"))
    num_list.append(my_num)
    count += 1
    if my_num > num:
        print("보다 작은 숫자를 입력하세요.")
    elif my_num < num:
        print("보다 큰 숫자를 입력하세요.")
    else: 
        print("정답숫자:",num)
        print("숫자입력 횟수:",count)
        print("입력숫자:",num_list)
        break

# 로또 맞추기 프로그램 구현하기
# 순서 : 임의 숫자, 숫자입력, 같은 숫자 금지, 정해진 범위 숫자, 선택한 숫자, 로또번호, 맞춘 숫자 표시
i = 0
count = 0
my_num = []
match = []
import random
lotto = random.sample(range(1,46),6)
while i < 6:
    my_num1 = int(input("선택번호:"))
    if my_num1 not in my_num:
        if my_num1 < 1 or my_num1 > 45:
            print("1~45번 사이 번호를 선택해 주세요.")
        else: 
            my_num.append(my_num1)
            i += 1
    else:
        print("이미 선택한 번호입니다.")

for i in my_num:
    if i in lotto:
        match.append(i)
        count += 1
print("로또번호:",lotto)
print("선택번호:",my_num)
print("맞춘개수:",count)
print("맞춘숫자",match)