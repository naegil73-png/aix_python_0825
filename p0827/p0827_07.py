# 리스트 : 자료형태 4가지(정수, 실수, 문자, 불린)를 저장할 수 있는 형태(리스트, 튜플, 딕셔너리) 중 하나이며, 원소로 여러개를 넣을 수 있음
# 변수에는 1개만 저장할 수 있으나, 리스트에는 여러개를 저장할 수 있음
# 리스트를 배열이라고도 함

a = 1
arr = [1,2,3,4,5]
print(a)
print(a+1)
print(type(a))
print(arr)
print(type(arr))
# print(arr+1) # 이런 형태로 합산은 안됨. 원소를 지정해서 합산해야 함
print(arr[1]+1)
# print(arr[9]+1) # 범위를 벗어나는 오류 발생
print(arr[2])

# 리스트의 길이 구하기
print(len(arr)) # 리스트 개수

# 리스트는 []로 시작
# 리스트는 여러개를 저장
# 리스트는 0부터 주소가 시작
# 리스트를 print하면 모두 출력가능
# 리스트의 특정주소로 그 값을 출력할 수 있음
# 리스트 개수 구하기 : len(리스트명)
# ******* 리스트 안에는 모든 타입을 넣을 수 있음 - 정수, 실수, 문자열, 불, 리스트, 튜플, 딕셔너리 등

# 리스트 추가가능한 타입 : 모든 타임
arr = [1, "안녕", 1.2, True, [1,2,3]]
print(arr[1])
print(arr[3])
print(arr[4])
print(arr[4][1])
a = arr[4]
print(a[1])

# # 1~10사이의 숫자 3개를 입력받아
# # 랜덤숫자를 맞추면 당첨, 그렇지 않으면 꽝

# import random
# num = random.randint(1,10)
# no1 = int(input("1.숫자 : "))
# no2 = int(input("2.숫자 : "))
# no3 = int(input("3.숫자 : "))
# print("입력숫자 :", no1,no2,no3)

# # 배열로 입력 숫자를 받는다면,
# num = [0,0,0]
# num[0] = int(input("1.숫자입력 : "))
# num[1] = int(input("2.숫자입력 : "))
# num[2] = int(input("3.숫자입력 : "))
# print("입력숫자:",num)

# # 위의 두 가지 경우는 반복문을 사용할 때, 큰 차이가 있음(맨 위의 것은 반복이 안됨)
# # 일반변수는 반복문을 사용하기 힘듬, 리스트는 반복문 사용가능

a = "사과"
b = "딸기"
c = "수박"
d = "참외"
e = "복숭아"

# a,b,c,d,e 중 참외가 있는 지 확인하고, 있으면 참외가 있습니다를 출력

if "참외"==a or "참외"== b or "참외" == c or "참외" == d or "참외" ==e:
    print("참외가 있습니다.")
else:
    print("참외가 없습니다.")

if "참외"==a:
    print("참외가 있습니다.")
elif "참외"==b:
    print("참외가 있습니다.")
elif "참외"==c:
    print("참외가 있습니다.")
elif "참외"==d:
    print("참외가 있습니다.")
elif "참외"==e:
    print("참외가 있습니다.")
else:
    print("참외가 없습니다.")

# 리스트
fruit = ["사과", "수박", "딸기", "참외", "복숭아"]
if "참외" in fruit:
    print("참외가 있습니다.")
else:
    print("참외가 없습니다.")

# 비교시는 리스트는 ("검색내용" in 리스트명)하면 됨

# import random
# r_num = random.randint(1,10)
# # 3개 숫자를 입력하여 리스트에 입력
# arr = []
# arr.append(int(input("1.1~10 숫자입력"))) # 리스트에 값을 추가
# arr.append(int(input("2.1~10 숫자입력"))) # 리스트에 값을 추가
# arr.append(int(input("3.1~10 숫자입력"))) # 리스트에 값을 추가

# if r_num in arr:
#     print("당첨")
# else:
#     print("꽝")
# print("추첨번호 : ",r_num,"선택번호 : ", arr)

# print("당첨" if r_num in arr else "꽝")

fruit = ["사과", "수박", "딸기", "참외", "복숭아"]
print(fruit[2]) # 인덱싱
print(fruit[1:4]) # 슬라이싱, 1,2,3
print(fruit[2:]) # 2부터 끝까지
print(fruit[:3]) # 처음부터 3번 앞까지
print(fruit[:]) # 모두 출력
print(fruit[::2]) # 2는 간격을 말함. 

# 슬라이싱 [시작:끝:간격]
arr = [1,2,3,4,5,6,7,8,9]
print(arr[::2]) # 홀수만 출력
print(arr[1::2]) # 짝수만 출력

# 마지막 앞까지 출력하려면..
print(arr[:-1]) # ******* 꼭 암기 마지막 제외 
print(arr[::-1]) # 리스트를 거꾸로 출력하라(리스트 역순정렬)

# 문자열 - 리스트형태로 저장
name = "안녕하세요반갑습니다"
print(name)
print(name[1])
print(name[-4])
print(name[6])
print(name[5:8])
print(name[-5:-2])
print(name[::2]) # ******* 꼭 암기

if "하" in name:
    print("있습니다")
else:
    print("없습니다")

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] # 2차원 배열

# p.195
arr = [[1,2,3],[4,5,6],[7,8,9]] # 2차원 배열
print(arr[1])
print(arr[1][1]) # 5를 출력하려면..

# p.196 IndexError

# p.197 리스트 연산
arr1 = [1,2,3]
arr2 = [4,5,6]
arr3 = arr1+arr2 # 리스트 + 리스트 = 리스트 합쳐짐. append 함수를 쓸 수도 있으나..

print(arr1+arr2) # 원래 리스트 내용을 변경하지 않음
print(arr3)

arr1.extend(arr2) # 원래 리스트 내용을 변경시킴
print(arr1)

arr4 = arr1*3 # 리스트의 반복
print(arr4)

aaa = [0,0,0,0,0,0,0,0,0,0]
aaa2 = [0]*10 # **** 중요, 꼭 암기
print(aaa)
print(aaa2)

# 리스트 추가 : append, insert
arr = [1,2]
arr.append(3) # 맨 마지막에 추가
arr.append(9) # 맨 마지막에 추가
arr.append(5) # 맨 마지막에 추가
print(arr)

# arr = [1,2,3,9,5]
arr.insert(1,20) # insert(위치, 추가할 요소) -> 잘 사용하지 않음. 맨 뒤에 공란을 만들고, 맨 뒤의 값을 공란에 넣고, 그 다음 값들을 하나씩 옮겨서 새값 추가
print(arr) # 작업이 많아져서 속도가 느려 insert를 잘 쓰지 않음

# 리스트 삭제 - del, pop, remove, clear(모두 삭제)
arr = [1,2,3,4,5]
# pop
arr.pop(2) # 3을 지우고 싶을 때, 자리 위치를 입력하면 3이 없어짐 -> 3 뒤에 있던 요소들이 한자리씩 이동함. 가급적 끝의 요소 제거가 효율적임
print(arr)

del arr[0] # 첫번째 자리 요소 제거, 슬라이싱으로도 제거 가능
print(arr)

# remove : 삭제할 값을 입력해서 삭제(위치가 아님)
arr.remove(2)
print(arr)

# 정렬 : 순차정렬(sort), 역정렬(sort(reverse=True)
arr = [1,5,8,3,2]
arr.sort()
print(arr)

arr = [1,5,8,3,2]
arr.sort(reverse=True)
print(arr)

arr = [1,3,5,7,9]
if 7 in arr:
    print("7이 있습니다.")
else:
    print("7이 없습니다.")

if 6 in arr:
    print("6이 있습니다.")
else:
    print("6이 없습니다.")

if 7 not in arr:
    print("7이 없습니다.")
else:
    print("7이 있습니다.")
