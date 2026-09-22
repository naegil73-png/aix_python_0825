a_list = ["딸기","바나나","사과"]
# 0: 딸기
# 1: 바나나
# 2: 사과 로 출력
# enumerate : 번호, 값 2개가 동시에 전달이 됨

a_list = ["딸기","바나나","사과"]
for i, value in enumerate(a_list):
    print("{}:{}".format(i, value))

for i in range(10): # range(1,11,2), 리스트, 문자열 등이 올 수 있음
    print(i)

# ******** 리스트 갯수를 만드는 방법 : 직접 갯수 지정, 요소+곱하기로 지정, len(길이)로 지정, range로 지정
alist = [] # 원소는 0개
print(len(alist))
alist2 = [0,0,0] # 원소는 3개
print(len(alist2))
alist3 = [0]*10 # 원소 1개에 10을 곱하면 10개인 리스트가 된다.
print(len(alist3))
alist4 = list(range(10)) # 0,10,....9
print(alist4)

alist5 = [i for i in range(10)] # 리스트 내포(for문으로 돌린 것을 리스트로 넣는 것), 아래의 다양한 형태로 만들 수도 있음
alist5 = [i+5 for i in range(10)] # 각 요소에 5를 더해서 리스트로 만드는 것
alist5 = [i*5 for i in range(10)] # 각 요소에 5를 곱해서 리스트로 만드는 것
alist5 = [i*i for i in range(10)] # 각 요소를 제곱해서 리스트로 만드는 것

# 반복하는 횟수가 있을 때는 for, 조건식이 있을 때는 while