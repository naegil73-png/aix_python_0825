# 타입변환
str2 = "111"
print(type(str2))
print(type(int(str2)))
# int(대상) - 정수형 변환, float(대상) - 실수형 변환, str(대상) - 문자열 변환, bool() - bool타입 변환

# 문자열 선언 : "", ''

# ""출력하고 싶을 때 \를 넣으면 뒤에 있는 것을 문자로 인식
print("안녕, 나는 \"홍길동\"이라고 해")

# \t:탭, \n: 줄바꿈
print("안녕\n하세요")
print("안녕"+"하세요") # +는 연결연산자
# print("안녕"+2) # st타입 + int타입 -> 에러
print("안녕"*10) # *는 반복연산자

# 문자슬라이싱
str1 ="안녕하세요" # 문자열은 각 요소별로 주소값이 있음
print(str1[1])

# [시작:끝:간격]
print(str1[::-1]) # 역순으로 출력
print(str1[:-1]) # 마지막은 제외하고 출력
print(str1[::2])

print(len(str1))