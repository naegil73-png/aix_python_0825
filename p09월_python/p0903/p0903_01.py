# C, 자바 : 컴파일러 언어 - 모든 소스를 기계어로 번역 후 프로그램 진행 -> 대체로 함수 등의 위치가 주요하지 않음. 코드 완성이 중요. 웹, 앱개발에 많이 사용
# 파이썬 : 스크립트 언어 - 한줄씩 기계어로 번역 후 프로그램 진행(순차진행) -> 시간이 다소 소요. 인공지능 등에 많이 사용
 # 함수들이 많으면, 복잡 -> 실행문을 밖으로 빼는 경우가 많음
# 함수 사용이유: 코드재사용, 코드 간결

# # ()가 있는 것은 대부분 함수 -> 함수 선언: def있음, 함수호출: def없음. 함수 실행은 함수호출에서 이루어짐
# def d_print():
#     for i in range(1,11):
#         print(i)

# def hello_print():
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")

# def cal(n1,n2):
#     print("{}+{}={}".format(n1,n2,n1+n2))
#     print("{}-{}={}".format(n1,n2,n1-n2))
#     print("{}*{}={}".format(n1,n2,n1*n2))
#     print("{}/{}={}".format(n1,n2,n1/n2))

# # -----
# hello_print()
# d_print()

# n1 = int(input("숫자입력:")) # 반드시 def cal(n1, n2)와 같은 이름 입력변수가 아니어도 됨. 위치에 따라 적용됨. 다만, 변수 갯수는 반드시 일치해야 함
# n2 = int(input("숫자입력:"))
# cal(n1,n2)

# # 이렇게 해도 됨
def d_print():
    for i in range(1,11):
        print(i)

def hello_print():
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")

# 두 수를 함수의 매개변수로 입력받아 사칙연산하는 구문
def cal(n1,n2):
    r1 = n1+n2 # 수식을 별개의 변수로 할당했으므로 return으로 r을 받아야 함
    r2 = n1-n2
    r3 = n1*n2
    r4 = n1/n2
    return r1,r2,r3,r4


# -----
hello_print()
d_print()

n1 = int(input("숫자입력:")) # 반드시 def cal(n1, n2)와 같은 이름 입력변수가 아니어도 됨. 위치에 따라 적용됨. 다만, 변수 갯수는 반드시 일치해야 함
n2 = int(input("숫자입력:"))
cal(n1,n2) # r1,r2,r3,r4 = cal(n1,n2)로 해도 됨
print("{}+{}={}".format(n1,n2,n1+n2))
print("{}-{}={}".format(n1,n2,n1-n2))
print("{}*{}={}".format(n1,n2,n1*n2))
print("{}/{}={}".format(n1,n2,n1/n2))

n1 = int(input("숫자입력:")) # 반드시 def cal(n1, n2)와 같은 이름 입력변수가 아니어도 됨. 위치에 따라 적용됨. 다만, 변수 갯수는 반드시 일치해야 함
n2 = int(input("숫자입력:"))
r1,r2,r3,r4 = cal(n1,n2)
print(r1,r2,r3,r4)
