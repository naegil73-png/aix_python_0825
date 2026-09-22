# str = input("번호 3개를 입력하세요:(123/5/23)")
# # 위 형태의 숫자 3개를 입력, 합을 구해서 출력하시오.

# total = 0
# str1 = str.split("/")
# for i in str1:
#     i = int(i)
#     total += i
# print(total)

# # ******** map함수 : map(함수, 반복리스트) -> 자료를 한꺼번에 변경하는 함수(map(명령어, 자료) 형태임)
# aa = ['1','2','3']
# aa2 = list(map(int,aa)) # aa에 있는 요소를 하나씩 숫자화해서(int) 리스트로 넣어라. -> map으로 실행하면, map자료형이므로 list형으로 만들어줘야 함
# print(aa2)

# print(list(map(int,aa))) # 이렇게 해도 됨

# # map, join함수는 문자열만 가능
# stu = [1,"홍길동",100,100,100] # 이 자료를 ','로 구분해서 문자열로 만들어라
# stu = list(map(str,stu)) # 한꺼번에 문자열로 변환
# stu1 = ",".join(stu)
# print(stu1)

# # 전개연산자
# str = input("날짜를 입력하세요.(2026/09/02)") # 
# str_arr = str.split('/')
# print("{}년 {}월 {}일".format(*str_arr))

print('1234'.isdigit()) # 숫자로 변환가능한 문자열인지 확인
a = int(input("숫자를 입력하세요.:")) # 숫자형 입력 않으면 에러 발생
a = input("숫자를 입력하세요.:") # 이런 형태로 작성해야 함
if a.isdigit():
    a = int(a)

# 실제 작성례 : 입력형식이 만족하는 지 확인하는 구문
while True:
    a = input("숫자를 입력하세요.:") # 이런 형태로 작성해야 함
    if a.isdigit():
        a = int(a)
        break
    else:
        print("숫자가 아닙니다. 다시 입력하세요.")