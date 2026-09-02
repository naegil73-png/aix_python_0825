a = "11"
print(int(a))
print(type(int(a)))

b = 1.12
print(int(b)) # 소수가 날아감
print(float(b))

c = 10
d = 3
e = 10/3
print(type(e))

e = 10//3 # 정수로 변환하려면
print(type(e))

f = 5
if f%2==0:
    print("짝수")
else: print("홀수")

result= "짝수"if f%2==0 else "홀수"
print(result)

# inch 입력받아 cm로 반환하는 구문
str_input = input("숫자입력: ")
num_input = int(str_input)
print(num_input, "inch")
print((num_input*2.54),"cm")

# 원의 둘레와 넓이 구하는 구문
str_input = input("원의 반지름 입력>")
num_input = int(str_input)
print()
print("반지름:", num_input)
print("둘레:", 2*3.14*num_input)
print("둘레: {:.1f}".format(2*3.14*num_input))
print("넓이:", 3.14*num_input**2)

