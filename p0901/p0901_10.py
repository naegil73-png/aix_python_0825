# 카드놀이

number= [1,2,3,4,5,6,7,8,9,10,11,12,13] # A, J, Q, K는 숫자로 변환
shape = ["SPADE", "HEART","DIAMOND","CLOVER"]
# 이 두 자료를 SPADE, 1, SPADE, 2,..... CLOVER, 13으로 출력

for i in shape:
    for j in number:
        print("{}{}".format(i,j))

n_shape = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
number= [1,2,3,4,5,6,7,8,9,10,11,12,13] # A, J, Q, K는 숫자로 변환
shape = ["SPADE", "HEART","DIAMOND","CLOVER"]
# 이 두 자료를 SPADE, 1, SPADE, 2,..... CLOVER, 13으로 출력

# card에 ["SPADE",1]... 형태로 출력
card = []

for i in shape:
    for j in number:
        card.append([i,j])
print(card)

# 카드를 섞으려면..
import random

n_shape = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
number= [1,2,3,4,5,6,7,8,9,10,11,12,13] # A, J, Q, K는 숫자로 변환
shape = ["SPADE", "HEART","DIAMOND","CLOVER"]

card = []

for i in shape:
    for j in number:
        card.append([i,j])
random.shuffle(card)
print(card)

# 타입 : 숫자형 - 정수, 실수, 문자열, 불
# 자료형태 : 리스트, 튜플, 딕셔너리
aa = [1,2,3,4,5]
aa2 = (1,2,3,4,5) # 튜플 : 수정이 안됨. 인덱싱 등 사용하는 것은 리스트와 같음
aa3 = {"key":"value",} # 딕셔너리 : key, value로 구성