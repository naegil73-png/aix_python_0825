# 람다식 - 함수요약
# 일반함수
def sum(n1,n2):
    result = n1+n2
    return result

print(sum(10,20))

# 람다식 - 1줄만 명령어가 있어야 함.
lambda n1, n2:n1+n2 # lambda - def 함수명 과 같음. 함수가 1줄이어야 사용 가능. 결과값이 1개여야 함. 결과값은 2개 불가
lambda n1:n1+10

sum = lambda n1, n2:n1+n2 # ,n1*n2를 뒤에 붙이면 안됨
print(sum(10,20))

lambda n1,n2:n1*n2

# map(함수, 리스트) : 특정 함수에 리스트를 적용해서 돌려줌
mlist = [1,2,3,4,5] # +10씩 반복적 더해주려면

# 기존방식
mlist2 = []
for i in mlist:
    mlist2.append(i+10)

# 기존방식 : 함수사용
def add(num):
    return num+10

a_arr=[]
for m in mlist:
    a_arr.append(add(m))

# 개선 : 리스트내포
a_arr = [m+10 for m in mlist]
print(a_arr)

# map 함수 사용 : lambda식 사용. map(함수, 리스트) 형식으로 사용
a_lam = lambda num:num+10
mlist=[1,2,3,4,5]

print()

mlist2 = list(map(a_lam,[1,2,3,4,5])) # 외울 것(lambda함수, map함수 사용례 ******* 이런 형태 사용 많이 함)
print(mlist2)

# 각 요소를 문자에서 숫자로 변환
data = ["100","200","300"]
result = map(int,data)
print(list(result))

# 문자열리스트 -> 숫자리스트로 변경

a= [1,2,3]
b = [10,20,30]
result = map(lambda x,y:x+y,a,b) # a, b를 각각 x, y에 입력해줌
print(list(result))

# 팩토리얼값을 구하는 함수
# 재귀함수 : 함수에서 자기 자신을 부르는 함수

def factorial(num):
    if num <= 1:
        return num
    else:
        result = num*factorial(num-1)
        return result

print(factorial(4))

# 재귀함수
def fact1(num):
    if num <= 1:return num
    else:return num*fact1(num-1)

