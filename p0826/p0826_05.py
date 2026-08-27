# 산술연산자 : +, -, *, /, //, %, **
# 산술계산 : *,/ 먼저 +,- 순으로 진행
# 우선순위에 있는 것은 괄호로 분리

print(2+2-2*2/2*2)
print(2-2+2/2*2+2)
# print("안녕"+3) -> 불가, 다른 타입 사칙연산 에러
print(1.1+5) # 숫자형에서 정수형과 실수형 사칙연산은 가능
print(int(1.9)) # 실수를 정수로 변환할 때, 소숫점이 삭제되므로 변환해도 되는 지 확인해야 함

# 문자열 연결연산(+), 반복연산(*)
print("안녕"+"하세요") # ***** 문자열 더하기는 연결의 의미
print("안녕"*10) # ***** 문자열 곱하기는 반복의 의미

# 문자열인데, 숫자형(문자열 숫자)은 숫자로 변환가능, 하지만, 문자형은 숫자로 변환 불가
str1, str2, str3 = "100", "1.123", "999"
# print(str1+1) # 불가능(문자열+숫자형)
print(int(str1)+1) # 문자열숫자는 자동변경이 안되므로 변경을 시켜줘야 연산 가능
print(float(str2)) # 소숫점 형태의 문자열 숫자는 float로 변경해줘야 함. int로 하면 에러발생
print(int(str3)+1)
# print(int("안녕")) # 에러가 발생(문자형은 숫자로 변경 불가)

# ******* 성적처리(매우 중요)
# # 번호, 이름, 국어, 영어, 수학을 입력받아
# # 번호, 이름, 국어, 영어, 수학, 합계, 평균을 출력하시오. 평균은 소숫점 둘째자리까지 표시
# # 결과 : 1 홍길동 100 100 100 300 100.0
num = input("번호를 입력하세요 : ")
name = input("이름을 입력하세요 : ")
kor = int(input("국어 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
math = int(input("수학 점수를 입력하세요 : "))
total = kor+eng+math
avg = total/3 # 나누기하면 실수형으로 바뀜

print("{} {} {} {} {} {} {}".format(num,name,kor,eng,math,total,avg))
print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(num,name,kor,eng,math,total,avg))

# 결과 위, 아래 줄을 그으려면
print("-"*60)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균".format(num,name,kor,eng,math,total,avg))
print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(num,name,kor,eng,math,total,avg))
print("-"*60)

# 1명을 추가하려면.. 2 유관순 100 100 98
num2 = input("번호를 입력하세요 : ")
name2 = input("이름을 입력하세요 : ")
kor2 = int(input("국어 점수를 입력하세요 : "))
eng2 = int(input("영어 점수를 입력하세요 : "))
math2 = int(input("수학 점수를 입력하세요 : "))
total2 = kor2+eng2+math2
avg2 = total2/3 # 나누기하면 실수형으로 바뀜

print("-"*60)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균".format(num,name,kor,eng,math,total,avg))
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(num,name,kor,eng,math,total,avg))
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(num2,name2,kor2,eng2,math2,total2,avg2))
print("-"*60)

# # 위의 함수에서 사람이 추가될 경우, for 문 등으로 사용 가능

print("101"+"102") # 문자열+문자열이므로 101102가 됨. print("안녕"+"하세요")의 결과와 동일

a = 10
a = a + 2
print(a)

# 이는 이렇게 약식으로 표현 가능
a = 10
a += 2 # = 앞의 'a +' 가 우변으로 적용된다 생각하면 혼동이 적을 듯(내 생각)
print(a)

# 원의 반지름을 입력받아
# 원의 넓이를 출력하세요.

# length = int(input("반지름을 입력하시오."))

# # 원 넓이 = pi(3.14)*length**2
# # 원의 넓이 : 100cm2
# # 원의 둘레 : 2*pi*length
# pi = 3.14

# result = pi*(length**2)
# result2 = 2*pi*length

# print("원의 넓이 {}cm2, 원의 지름{:.2f}cm".format(result, result2))