# 입력한 숫자까지 합계
# # for문만으로도 사용할 수 있으나, 재사용이 곤란 -> 재사용이 많을 것 같으면 함수 사용

# def add():
#     num = int(input("숫자를 입력하세요.:"))
#     sum = 0
#     for i in range(1,num+1):
#         sum += i
#     print(sum)

# for i in range(10):
#     add()

# def add2(num2):
#     sum = 0
#     for i in range(1,num2+1):
#         sum += i

#     print(sum)

# for i in range(10):
#     num2 = int(input("숫자 입력:"))
# add2(5)


# def add3(num3,num4):

#     sum = 0
#     for i in range(num3,num4):
#         sum += i
#     print(sum)

# for i in range(10):
#     num3 = int(input("숫자입력:"))
#     num4 = int(input("숫자입력:"))
# add3(3,5)

def add4(num5,num6):
    sum = 0
    for i in range(num5,num6+1):
        sum += i
    return sum

for i in range(10):
    num5 = int(input("숫자입력"))
    num6 = int(input("숫자입력"))
    sum = add4(num5,num6)
    print(sum)