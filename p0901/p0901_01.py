# 구구단
for i in range(2,9+1):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))
    print()

# 1~100사이의 숫자 맞추기
# 사고 순서 : 랜덤번호 생성 -> 숫자를 입력받기 -> 맞출 때까지 무한으로 입력받기 -> 숫자비교 -> 결과 출력
# for문은 반복/횟수지정, while문은 조건, 또는 무한루프(반복)일 때 사용(올바른 입력값을 입력토록 하는 경우에 사용)
import random
ran_no = random.randint(1,101)
in_arr = []
while True:
    in_no = int(input("숫자입력:"))
    in_arr.append(in_no)
    if in_no == ran_no:
        print("정답입니다.")
    elif in_no < ran_no:
        print(in_no,"보다 큰 숫자를 입력하세요.")
    else:
        print(in_no,"보다 작은 숫자를 입력하세요.")
        break
print("입력한 모든 리스트 : ",in_arr)
print("정답 :", ran_no) # 입력값의 마지막으로 해도 됨
print("정답 :", in_arr[-1]) # 입력값의 마지막으로 해도 됨
print("정답 :", in_no) # 입력값의 마지막으로 실행된 것으로 해도 됨







# 1~100사이 숫자 맞추기, 입력한 값들도 출력
# 1.랜덤번호 1개 생성
# 2.무한으로 입력받기
# 3.숫자 입력 받기
# 4.랜덤숫자와 숫자 비교
# 5.결과 출력

import random
r_num = random.randint(1,101)
input_num = []
count = 0
while True:
    m_num = int(input("숫자입력:"))
    input_num.append(m_num)
    count += 1
    if m_num == r_num:
        print(m_num,"정답입니다.")
        break
    elif m_num > r_num:
        print(m_num,"작은 수를 입력하세요.")
    else:
        print(m_num,"큰 수를 입력하세요.")
print("입력한 수:",input_num,"정답:",r_num,count,"번만에 맞추셨습니다.")