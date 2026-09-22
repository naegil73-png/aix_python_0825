for i in range(3):
    print(i)

for i in range(1,5+1): # +로 표현해도 됨
    print(i)

for i in range(0,11,2): # 2씩 증가해서 적용
    print(i)
print("-"*10)

'''
# 이름 입력을 3번 반복하시오.
for i in range(3):
    name = input("이름입력:")
    print(name)
'''

# [학생명단]
# 홍길동
# 유관순
# 이순신
# name = []
# for i in range(3):
#     name.append(input("이름:"))
# print("학생명단:",name)


# # 가급적 이런 형태로 출력
# name = []
# for i in range(3):
#     name.append(input("이름:"))
# print("학생명단:",name)
# name = []
# for i in range(3):
#     name.append(input("이름:"))
# for i in range(3):
#     print("학생명단:",name)

# for i in range(1,11):
#     print(i)


# 10, 20, 30, .... 100 출력되게 작성
for i in range(1,11):
    print(i*10)

# 리스트 각 원소를 하나씩 출력하려면..
arr = [1,3,5,7] 
for i in arr:
    print(i)
# 또는    
arrs = [1,3,5,7]
for arr in arrs:
    print(arr)

fruits = ["사과","배","바나나"]
for f in fruits:
    print(f)

# 리스트 원소 하나씩 출력
nums = [3,9,10,105,220,2,1]
for num in nums: # ***** 뒤에는 range, 범위(a,b), 리스트, 문자가 온다
    print(num)

for i in "안녕하세요":
    print(i)

# # 입력한 숫자가 홀수인지, 출력하시오.

# num = int(input("입력숫자:"))
# if num%2==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

# 위의 리스트가 3: 홀수, 9: 홀수, 10: 짝수... 이렇게 표현되도록 작성
nums = [3,9,10,105,220,2,1]
for num in nums:
    if num%2 == 0:
        print(num,"짝수입니다.")
    else:
        print(num,"홀수입니다.")

# indent rainbow (들여쓰기 등에 유용)

# 위의 리스트에서 짝수인 경우만 출력하려면..
nums = [3,9,10,105,220,2,1]
for num in nums:
    if num%2 == 0:
        print(num,"짝수입니다.")
    else:
        pass

# 반복문
# ******** for i in range(10) / range(1,11) / range(1,11,2) / [1,2,3] / "안녕하세요" -> in 다음에 range, 범위, 리스트, 문자열 올 수 있음

# print 시 줄바꿈 대신 옆으로 출력하려면, end = ""로 하면 됨
print(1, end = " ")
print(2, end = " ")
print(3)

print(1, end = "\t")
print(2, end = "\t")
print(3)
print(4)

# # *********** for 문에서 가장 기본 : 구구단 출력
# for i in range(2,10):
#     print(i,"X",1,"=",i*1) # 많이 사용하는 유형
#     print("{} X {} = {}".format(i,1,i*1))

for i in range(2,10):
    print("{}단".format(i))
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
        print("{} X {} = {}".format(i,j,i*j))

# 옆으로 나오게 하려면..
for i in range(2,10):
    print("{}단".format(i))
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j),end = "  ")
    print()


for i in range(2,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j),end = "\t")
    print()