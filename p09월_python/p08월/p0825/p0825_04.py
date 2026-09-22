# 이제부터 매우 중요

# 변수는 값을 저장하는 공간(그릇) : 필히 기억할 것
# 변수 타입은 값을 입력할 때 정해짐
# 변수는 변수에 어떤 것을 입력하느냐에 따라 변수 타입이 결정됨(4가지 타입이 있음(기억할 것) : 불(참거짓)타입, 정수, 실수, 문자)

a = 10 # 숫자형타입 - 정수 타입
b = 10.1 # 숫자형타입 - 실수 타입(소수점), 연산이 반복되어 커질수록 문제가 커질 수 있음. 소수점 삭제 등에 유의해야 함
aa = "안녕" # 문자열타입
abc = True # 불타입(bool) - True, False만 가능, boolean

# 변수명은 뭐라도 가능하나, 예약어(프로그램이 사용하는 명령어, ex) print)는 변수로 사용할 수 없음. True, False같은 변수 명도 안됨

print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10//5) # 몫
print(10%5) # 나머지
print(10**5) # 5제곱

# p.85
print(9+4)
print(9-4)
print(9*4)
print(9/4)
print(9//4)
print(9%4)
print(9**4)

# 계산에서 수식은 동일하나, 적용할 값이 달라질 경우 변수 지정이 유용.(함수를 이용해서 입력변수에 따라 쉽게 적용 가능)

a = 10
b = 5
c = "안녕"
d = True

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # 몫
print(a%b) # 나머지
print(a**b) # 5제곱

# 변수 타입 확인 : type 표시 알아둘 것. int, float, str, bool
print(type(a))
print(type(b))
print(type(a+b))
print(type(a/b))
print(type(c))
print(type(d))

# 키워드 리스트(p.70)
import keyword
print(keyword.kwlist)

