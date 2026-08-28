# 조건문 안에 조건문
# if문 안에 if문이 올 수 있음(대체로 2번까지 사용, 예외적으로 3번까지 사용 -> 많이 쓰면 속도가 느려짐)

a = 1
if a>50:
    if a<100:
        print("50보다 크고, 100보다 작은 수")
    else: 
        print("50보다 크고, 100보다도 큰 수")
else:
    print("50보다 작은 수")

# 조건문을 여러개
score = 65

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")

# 임의의 수가 양수인지, 음수인지 판정
import random

num = random.randint(-3,3)
if num > 0:
    print("랜덤숫자 :",num, "양수입니다")
elif num<0:
    print("랜덤숫자 :",num, "음수입니다")
else:
    print("랜덤숫자 :",num, "0입니다")


# 0~100점까지 랜덤숫자 생성
# 60점 이상은 합격
# 50~59점은 재시험
# 0~49점은 불합격으로 출력되도록 작성

import random
score = random.randint(0,100)

if score >= 60:
    print(score, "점, 합격입니다")
elif score >=50: # 59>=score>=50 으로도 가능(두번을 확인해야 해서 시간이 0.1초 정도 더 걸림)
    print(score,"점, 재시험입니다")
else:
    print(score,"점, 불합격입니다")
print("랜덤점수 : ", score)

# 랜덤점수를 생성해서
# 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 60미만은 F
# 랜덤점수를 출력하시오.

import random
score = random.randint(0,100)

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
print("랜덤점수 : ",score)

# 랜덤점수를 생성해서
# 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 60미만은 F이고
# 90~92 A-, 93~97 A, 98~ A+
# 80~82 B-, 83~87 B, 88~ B+
# 70~72 C-, 73~77 C, 78~ C+
# 60~62 D-, 63~67 D, 68~ D+


# 랜덤점수를 출력하시오.

import random
score = random.randint(0,100)

if score >=90:
    if score>=98:
        print("A+")
    elif score >=93:
        print("A")
    else: 
        print("A-")
elif score >=80:
    if score>=88:
        print("B+")
    elif score >=83:
        print("B")
    else: 
        print("B-")
elif score >= 70:
    if score>=78:
        print("C+")
    elif score >=73:
        print("C")
    else: 
        print("C-")
elif score >=60:
    if score>=68:
        print("D+")
    elif score >=63:
        print("D")
    else: 
        print("d-")
else:
    print("F")
print("랜덤점수:",score)

# if : 조건문
# 구조 : if-else, if-elif-else, if-elif-elif-else...
# if + 조건문:
#   들여쓰기 되어야 함(내용을 입력해야 함. 없으면 에러 발생. 입력하고 싶지 않을때는 pass를 쓰면 됨)
# else:
#   들여쓰기 되어야 함

if 10>5:
    pass # 결과를 내고 싶지 않을때.
if 10>5: pass
if 10>5: print("참") # 한줄로 표시 가능. 다만, 두줄이상이면 다음줄에 입력해야 함

# if 10>5: print("참")
#     print("좋아요") # 이런 형태면 에러가 발생함

# 날짜함수를 사용하려면..
import datetime

now = datetime.datetime.now()
# 해당월에 따라 봄, 여름, 가을, 겨울이라고 출력하시오.
# 겨울 12,1,2, 봄 3,4,5, 여름 6,7,8, 가을 9,10,11
# 비교문을 사용해서 
# 해당월 계절을 출력하시오

month = now.month
if 3<=month<6:
    print("봄")
elif 6<=month<9:
    print("여름")
elif 9<=month<12:
    print("가을")
else:
    print("겨울")

# # 월을 직접 입력해서 계절을 알려고 하면..

# # 해당월에 따라 봄, 여름, 가을, 겨울이라고 출력하시오.
# # 겨울 12,1,2, 봄 3,4,5, 여름 6,7,8, 가을 9,10,11
# # 비교문을 사용해서 
# # 해당월 계절을 출력하시오

# month = int(input("월:"))
# if 3<=month<6:
#     print("봄")
# elif 6<=month<9:
#     print("여름")
# elif 9<=month<12:
#     print("가을")
# else:
#     print("겨울")

# month = int(input("월:"))
# if month == 12 or month == 1 or month ==2:
#     print("겨울")
# elif 3<=month<6:
#     print("봄")
# elif 6<=month<9:
#     print("여름")
# else:
#     print("가을")

score = 65
# score 60점 이상이면 합격, 미만이면 불합격
if score >= 60: print("합격") # 명령문이 1줄이어서 축약
else: print("불합격") # 1줄로 축약

# 위의 것을 1줄로 작성, if문 축약
result="합격" if score >=60 else "불합격"

# 리스트 : 자료형태 4가지(정수, 실수, 문자, 불린)를 저장할 수 있는 형태(리스트, 튜플, 딕셔너리) 중 하나이며, 원소로 여러개를 넣을 수 있음
# 변수에는 1개만 저장할 수 있으나, 리스트에는 여러개를 저장할 수 있음
