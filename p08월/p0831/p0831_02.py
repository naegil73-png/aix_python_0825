# 구구단을 아래로 출력하시오.

for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print()

# 옆으로 출력
for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j, end="\t")

# 옆으로 출력, 단 간의 줄바꿈
for i in range(2,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j), end="\t")
    print()

# 단간의 배열을 옆으로
for i in range(1,10):
    for j in range(2,10):
        print("{} X {} = {}".format(j,i,i*j), end="\t")
    print()
    print()

for i in range(1,10):
    print(f"[{i}단]")
    for j in range(2,10):
        print("{} X {} = {}".format(j,i,i*j), end="\t")
    print()

# 1~10을 더해서 '합계 : 55'로 출력
total = 0
for i in range(1,11):
    total = total+i
print("합계:",total)

mul = 1
for i in range(1,11):
    mul = i*mul
print("곱셈: {:,d}".format(mul))

# 합, 곱셈을 같이 표현
total = 0
mul = 1
for i in range(1,11):
    total = total+i
    mul = i*mul
print("합계:",total)
print("곱셈: {:,d}".format(mul))

# 100을 넘는 숫자와 합계
sum = 0
for i in range(1,100):
    sum = sum + i
    if sum > 100:
        print("{}까지 합계는: {}".format(i,sum))
        break # for문을 정지해줌(강제종료)
# 
sum = 0
no = 0
for i in range(1,100):
    sum = sum + i
    if sum > 100:
        no = i
        sum2 = sum
        print("{}까지 합계는: {}".format(no,sum2))
        break # for문을 정지해줌(강제종료)

# 100 이전 단계의 수, 그 때까지의 합계
sum = 0
no = 0
for i in range(1,100):
    sum = sum + i
    if sum > 100:
        no = i
        sum2 = sum
        print("{}까지 합계는: {}".format(no-1,sum2-no))
        break # for문을 정지해줌(강제종료)

# 100 초과한 수 이후의 수와 그 때까지의 합계
sum = 0
no = 0
for i in range(1,100):
    sum = sum + i
    if sum > 100:
        no = i
        sum2 = sum
        print("{}까지 합계는: {}".format(no+1,sum2+no))
        break # for문을 정지해줌(강제종료)

# 1에서 100까지의 합을 구하시오.
sum = 0
for i in range(1,101):
    sum = sum + i
print("합:",sum)

# 1에서 100까지의 홀수 합을 구하시오.
sum = 0
num = 0
for i in range(1,101,2):
    sum = sum + i
    num += 1
print("합:",sum, "합한 횟수", num)

# # 1에서 100까지의 7의 배수만 합을 구하시오.
# sum = 0
# num = 0
# for i in range(0,101,7):
#     sum = sum + i
#     num += 1
# print("합:",sum, "합한 횟수", num)

# sum = 0
# num = 0
# for i in range(1,101):
#     if i%7==0:
#         sum = sum+i
#         num += 1
# print("합계:",sum, "합한 횟수:",num)

# # for문을 이용해서 3개의 입력한 숫자의 합을 구하시오.
# # 반복문, 하나의 입력문장, 입력값의 숫자화, 초기변수 값, 합산식

# sum = 0
# for i in range(3):
#     a = int(input("숫자1:"))
#     sum = sum + a
# print("합계: {}".format(sum))

# # 입력한 값도 같이 출력하려면..
# # 위의 내용에서 list 필요

# sum = 0
# num = []
# for i in range(3):
#     a = int(input("숫자1:"))
#     sum = sum + a
#     num.append(a)
# print("합계: {}, 입력한 값{}".format(sum,num))

sum = 0
for i in range(1,11):
    sum += i
print("합:",sum)

# # 입력한 첫번째 숫자부터 두번째 입력한 숫자까지 합을 구하시오.
# sum = 0
# a = int(input("숫자1:"))
# b = int(input("숫자2:"))
# for i in range(a,b):
#     sum += i
# print('합계:',sum)

# # 만약, a>b이면 합계는 0이 나옴. 이럴 경우 해야하는 처리 -> 값을 서로 변경해야 함
# sum = 0
# a = int(input("숫자1:"))
# b = int(input("숫자2:"))
# c = 0
# if a>b:
#     c = a
#     a = b
#     b = c
# for i in range(a,b):
#     sum += i
# print('합계:',sum)

# sum = 0
# a = int(input("숫자1:"))
# b = int(input("숫자2:"))
# c = 0
# if a>b:
#     a,b = b,a
# for i in range(a,b):
#     sum += i
# print('합계:',sum)

# 구구단을 출력
for i in range(2,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))
    print()

for i in range(2,10):
    for j in range(1,10):
        print(f"{i} X {j} = {i*j}")
    print()

# # 숫자 입력을 받아 그 단부터 출력하시오.

# num = int(input("입력숫자:"))
# for i in range(num,10):
#     for j in range(1,10):
#         print(f"{i} X {j} = {i*j}")
#     print()

# # 5단까지만 출력     
# num = int(input("입력숫자:"))
# for i in range(num,num+1): # 또는 (num, 10)으로 하고, if문에서 i == 5이면, break문을 써도 됨
#     for j in range(1,10):
#         print(f"{i} X {j} = {i*j}")
#     print()

# # a, b 두 숫자 입력을 받아 a단부터, 각 단은 b곱하기까지 출력하시오.

# num = int(input("입력숫자1:"))
# num1 = int(input("입력숫자2:"))
# for i in range(num,10):
#     for j in range(1,num1+1):
#         print(f"{i} X {j} = {i*j}")
#     print()

# # 리스트에서 항목 추가
# list_a = ["바나나", "딸기", "사과"]
# list_a.append(input("과일이름:"))

# # 리스트에 for문 이용해서 3개를 추가하려고 하면..
# # for문은 같은 구문 반복, 추가 구문, 3번 반복, 리스트에 추가는 append

# list_a = ["바나나", "딸기", "사과"]
# for i in range(3): # 추가 구문을 3번 반복한다.
#     list_a.append(input("과일이름:"))
# for i in list_a:
#     print(i)

# 리스트를 순서대로 출력하려면
list_a = ["바나나", "딸기", "사과"]
for i in list_a:
    print(i)

# 1:바나나, 2:딸기, 3:바나나로 출력하고 싶다면..
j = 1
list_a = ["바나나", "딸기", "사과"]
for i in list_a:
    print(j,":",i)
    j = j + 1

# 위의 방법이 번거로움 -> ******* enumerate 함수 : index번호(0부터 시작함)와 리스트 값 2개를 반환함
for i,value in enumerate(list_a):
    print(i+1,":",value)

for i in range(3):
    print(i+1,":",list_a[i])

# 리스트의 원소 수가 변경되어 4개가 되거나 5개로 변경된다고 하더라도 모든 요소가 출력되게 하려면..
# 리스트 원소 길이만큼 반복하게 하면 됨
for i in range(len(list_a)):
    print(i+1,":",list_a[i])


for i in range(1,4):
    print(i)

print("for문 밖 i : ",i+5)

for i in range(1,4):
    print(i) 

# # 이름, 국어점수를 3개 받아서 출력
# # [학생성적]
# # 홍길동 70
# # 유관순 100
# # 이순신 90

# list_1 = []
# name = []
# kor = []
# for i in range(3):
#     name.append(input("이름:"))
#     kor.append(int(input("국어점수:")))
# print("[학생성적]")
# for i in range(len(name)):
#     print(f"{name[i]}\t{kor[i]}")

# # 위에서 영어점수, 수학점수 추가
# list_1 = []
# name = []
# kor = []
# eng = []
# math = []
# for i in range(3):
#     name.append(input("이름:"))
#     kor.append(int(input("국어점수:")))
#     eng.append(int(input("영어점수:")))
#     math.append(int(input("수학점수:")))
# print("[학생성적]")
# print(f"이름\t국어\t영어\t수학")

# for i in range(len(name)):
#     print(f"{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}")

# # 위에서 합계, 평균 추가 -> 계산이 추가 -> 리스트로 계산 불가
# name = []
# kor = []
# eng = []
# math = []
# total = []
# avg = []
# for i in range(3):
#     name.append(input("이름입력 :"))
#     k_input = int(input("국어점수입력 : "))
#     kor.append(k_input)
#     e_input = int(input("영어점수입력 : "))
#     eng.append(e_input)
#     m_input = int(input("수학점수입력 : "))
#     math.append(m_input)
#     total.append(k_input+e_input+m_input)
#     avg.append((k_input+e_input+m_input)/3)

# print("[ 학생성적 ]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t")
# print("-"*60)
# for i in range(len(name)):
#     print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\
# \t{total[i]}\t{avg[i]:.2f}")

# # 위의 구문을 이렇게 작성하면 안됨. 합계는 리스트+리스트가 되고, 평균은 typeerror 발생
# name = []
# kor = []
# eng = []
# math = []
# total = []
# avg = []
# for i in range(3):
#     name.append(input("이름입력 :"))
#     kor.append(int(input("국어점수입력 : ")))
#     eng.append(int(input("영어점수입력 : ")))
#     math.append(int(input("수학점수입력 : ")))
#     total.append(kor+eng+math)
#     avg.append((kor+eng+math)/3)

# print("[ 학생성적 ]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t")
# print("-"*60)
# for i in range(len(name)):
#     print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\
# \t{total[i]}\t{avg[i]:.2f}")

