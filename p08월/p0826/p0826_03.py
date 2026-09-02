num1 = 100
num2 = 100
num3 = 100

print(num1, num2, num3)

num4 = num5 = num6 = 1
print(num4, num5, num6)

# a1=1, a2="안녕" # 값이 다른 것은 한줄에 넣을 수 없다. 병렬해서 넣을 수 없음
# print(a1, a2) # 에러가 남

a = 1
b = "안녕"
print(a, b)

a1=1
a2=2 
print(a1, a2) # 에러가 안남

no1 = 100 # 변수선언과 동시에 값 전달
print(10==10) # 같다 표현은 ==

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

# print: 출력을 의미
# input: 입력을 의미

# num = input("숫자를 입력하세요") # num의 결과는 str임
# print("입력숫자 : {}".format(num))

# 문자, 숫자 등 입력 형태를 요청하도록 하는 명령문
# input으로 받는 모든 것은 문자열타입임
# a = input("1번째 숫자를 입력하세요.")
# b = input("2번째 숫자를 입력하세요.")
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)

# # 문자열을 숫자로 변경해야 함
# a = int(input("1번째 숫자를 입력하세요.")) # 숫자같은 문자만 숫자로 변경함. 문자열인 문자는 숫자로 변경 불가 -> 문자를 입력하면 에러 발생
# b = int(input("2번째 숫자를 입력하세요."))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)

# 프로그램 개발 시 : 문자열을 받아서 숫자로 받을 수 있는 문자열인지 판정하는 조건문이 필요

# 아이디, 패스워드를 입력받아 출력하시오
# 아이디 : aaa, 패스워드 : 1111
# id = input("아이디 : ")
# pw = int(input("패스워드 : "))
# print("아이디 확인 : {}".format("aaa"==id))
# print("패스워드 확인 : {}".format("1111"==pw))
# print("aaa" == id)
# print("1111"==pw)
# print("아이디 : {}, 패스워드 : {}".format(id, pw))
# 로그인 시 id에 따른 pw값 일치 여부 확인(딕셔너리를 통해서 id가 있는 지 그리고 id:pw 조합으로 일치 여부 확인 조건문 설정)