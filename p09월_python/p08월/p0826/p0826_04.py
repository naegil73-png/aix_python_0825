# 송금금액 : 100 입력 받고
# 현 잔액 : 1000
# 총금액을 출력하시오.

# total1 = 1000
# send = int(input("송금금액을 입력하세요. : "))
# total2 = total1+send

# print("잔액 : {}, 송금금액 : {}, 총금액 : {}".format(total1, send, total2))

# print("잔액 : ",total1) # 이렇게로도 출력 가능 # 실수인 경우, 자릿수 변경은 불가(format으로만 가능)
# print("송금금액 : ",send) # 이렇게로도 출력 가능
# print("총금액 : ",total2) # 이렇게로도 출력 가능

# 국어, 영어, 수학점수를 입력받아
# 합계, 평균을 출력하시오.
# 합계: 300, 평균 : 100

# name = input("이름을 입력하세요.: ")
# kor = int(input("국어점수를 입력하세요 : "))
# eng = int(input("영어점수를 입력하세요 : "))
# math = int(input("수학점수를 입력하세요 : "))
# total = kor+eng+math
# avg = total/3

# print("이름: {}, 합계: {}, 평균: {:.2f}". format(name, total, avg)) # 바코드 같은 원리, 스캔을 하는 것이 input하는 작업임

a, b =1, 2 # a = 1, b = 1 -> 한줄에 이렇게 변수 지정하면 에러남(따로따로 변수 선언은 불가), a,b = 1, 2와 같이 한꺼번에 변수 선언은 가능(파이썬만 가능)
print(a,b)

# 진수 : 거의 안씀. 대용량데이터 처리 시 이진수를 씀
print(bin(5)) # 결과에서 0b는 이진수라는 의미임. ob101(2진수에서 101이라는 의미임). bin()은 2진수로 변경하는 명령어

print(int("101",2)) # 2진수 101을 10진수로 변경해줌

print(100**10)

# 지수표현식
a = 3.14
b = 3.14e5 # 3.14곱하기 10(e)의 5제곱
print(a, b)

a, b = 9, 2
print(a**b, a%b, a//b)
print(a/b)
print(a//b)
print(a%b)

# a = 5
# 짝수, 홀수인지?
print(a%2==1) # 홀수인지, 짝수인지 확인

a = int(input("숫자를 입력하세요.: "))
print(a%2==1) # 입력값을 기준, 조건을 적용해서 분류할 수 있음(잔고, 번호 등)

a = (100==100)
print(type(a))