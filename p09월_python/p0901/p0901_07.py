# 리스트 : 변수 1개에 하나의 값만 저장가능 -> 불편, 한개 변수에 여러개 값 저장, 복사할 수 있음, 반복문도 가능
a,b,c,d = 0,0,0,0 # 이를 각각 출력하려면, 아래와 같이 출력해야 함 -> 원소 추가 시 추가와 출력도 별도 추가해야 함, 출력도 개별로 합해줘야 함
print(a)
print(b)
print(c)
print(d)
print("-"*50)

a_arr = [10,20,30,40,50,60,70,80,90,100] # 리스트는 원소만 추가해주면 가능
for a in a_arr:
    print(a)

# a_arr에서 몇 개 원소만 가져오고 싶으면
print(a_arr[:3])

# a_arr 내 원소 합을 구하려면
total = 0
for i in a_arr:
    total += i
print(total)

# 리스트 추가 : append(뒤에 추가), insert(위치지정), extend(리스트+리스트)
# 리스트 수정 : a_arr[위치] = 새 값
# 리스트 삭제 : pop(위치): 위치가 없으면 제일 뒤의 요소 삭제, del 자료위치

a_list = [1,2,3]
a_list.append(4)
print(a_list)

a_list.pop() # 위치지정 없으면 맨 마지막 것 삭제
print(a_list)
a_list.pop(0) # 첫번째 요소 삭제
print(a_list)

# 퀴즈
n_arr = [100,91,230,1,2,5,70,500]
# 100이상의 숫자만 출력하시오.
num = []
for i in n_arr:
    print(i)
    if i >= 100:
        num.append(i)
print(num)

# 출력을 100: 3자리숫자, 91:2자리숫자
# 숫자는 길이가 없고, 문자만 있음 -> 숫자의 자릿수를 반환하려면, 숫자를 문자로 변환해야 함
n_arr = [100,91,230,1,2,5,70,500]
for i in n_arr: # i는 정수형
    no = str(i) # 문자형으로 전환. st = len(str(i))로 간단히 해도 됨
    num_len = len(no)
    print(i,f"{num_len}자리숫자")

# 출력결과를 리스트로 추가하고 싶다면
n_arr1 = []
n_arr = [100,91,230,1,2,5,70,500]
for i in n_arr: # i는 정수형
    no = len(str(i)) # 문자형으로 전환. no = len(str(i))로 간단히 해도 됨
    a = "{}:{}자리숫자".format(i,no)
    n_arr1.append(a)
print(n_arr1) 

# 입력, 출력, 수정, 삭제