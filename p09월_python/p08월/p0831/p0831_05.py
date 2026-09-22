# # break문 : 반복문을 완전히 종료
# # continue : 반복문을 1번만 제외(지정된 조건에 만족할 경우), 이후 계속 반복

# # for i in range(100):
# #     print(i)
# #     if i == 50:
# #         break # 50번만 진행함

# # print("프로그램 종료")

# # for i in range(100):
# #     print(i)
# #     if i == 50:
# #         continue # 50번일 때, skip하고 나머지는 다시 그대로 수행함

# # print("프로그램 종료")

# # # # 1~100사이의 숫자 중 홀수만 출력
# # # for i in range(100):
# # #     if i%2 ==0: # 짝수라면
# # #         continue # 건너뛰고 다시 수행하라
# # #     print(i)

# # no = []
# # name = []
# # i = 1
# # while True:
# #     n = input("{}.이름입력:".format(i))
# #     if n == 0:break
# #     name.append(n)
# #     no.append(i)
# #     i = i+1

# # 1~100까지 랜덤숫자 1개를 생성

# import random
# ran1 = random.randint(1,100)
# print("랜덤숫자:",ran1)

# # random숫자를 맞출 때까지 무한반복
# import random
# ran1 = random.randint(1,5)
# mynum = 0
# while True:
#     mynum = int(input("1~100사이 숫자를 입력:"))
#     print(mynum)
#     if mynum == ran1:
#         print("정답입니다.")
#         break
# print("프로그램 종료")

# random숫자를 맞출 때까지 무한반복
# 힌트를 주어서 입력한 숫자가 큰지, 작은지를 표시
# 입력했던 숫자를 모두 출력하고자 한다. -> 입력 숫자를 저장해야 함 -> append로 추가해줘야 함

# 구문 기획 : random 함수, randint, 입력한 숫자, 비교 및 모아서 출력

import random
randnum = random.randint(1,100)
my_list = []
mynum = 0
answer = 0
while True:
    mynum = int(input("1~100사이 숫자를 입력:"))
    my_list.append(mynum)
    print(mynum)
    if mynum == randnum:
        answer = mynum
        print("정답입니다.")
        break
    elif mynum > randnum:
        print("입력 숫자가 큽니다. 작은 숫자 입력")
    else: 
        print("입력 숫자가 작습니다. 큰 숫자 입력")
print("정답: ", answer)
print("정답: ", my_list[-1])
print("프로그램 종료")