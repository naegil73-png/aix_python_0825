for i in range(1,10,2):
    print(i)

# # 이름 입력 3번 하는 for문

# for i in range(3):
#     name = input("이름:")
#     print(name)

# # 3명 이름을 리스트로 받는 구문
# n_list = []
# for i in range(3):
#     n_list.append(input("이름:"))
# print("이름:", n_list)

# # 위의 형태보다 입력을 다 받고, 한꺼번에 출력하는 방식
# n_list = []
# for i in range(3):
#     n_list.append(input("이름:"))
# for i in range(3):
#     pass
# print("이름:",n_list)

# [1,3,5,7,9]를 하나씩 출력
a = [1,3,5,7,9]
for i in a:
    print(a)

# # '안녕하세요'를 한 글자씩 출력
# for i in "안녕하세요":
#     print(i)

# # 입력한 수가 홀수인지, 짝수인지 출력
# num = int(input("숫자:"))
# if num%2 ==0:
#     print("짝수")
# else:
#     print("홀수")

# 3,9,10,105,220,2,1 를 홀수인지, 짝수인지 출력
num = [3,9,10,105,220,2,1]
for i in num:
    if i%2 == 0:
        print(i,"짝수")
    else:
        print(i,"홀수")

# 짝수인 경우만 출력하려면..
num = [3,9,10,105,220,2,1]
for i in num:
    if i%2 == 0:
        print(i,"짝수")
    else: pass

# 구구단을 작성

for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print()

# 구구단을 단 배열을 옆으로 작성

for i in range(1,10):
    for j in range(2,10):
        print(j,"*",i,"=",j*i,end="\t")
    print()

# 1~10까지 합계, 곱
total = 0
mul = 1
for i in range(1,11):
    total += i
    mul *= i
print("합계:{},곱:{:,d}".format(total,mul))

# 1부터 더하여 합계가 100을 넘는 수와 그 합계
total = 0
for i in range(1,100):
    total += i
    if total > 100:
        print("숫자",i,"합계",total)
        break

# 임의의 숫자 3개를 합과 곱을 구하고, 입력한 값도 같이 출력하시오.

total = 0
mul = 1
num = []

for i in range(3):
    num1 = int(input("숫자:"))
    total += num1
    mul *= num1
    num.append(num1)
print("입력숫자:",num,"합:",total,"곱:",mul)