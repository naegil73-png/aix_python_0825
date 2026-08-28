# format함수
a = 10
print("{}".format(a))
print("{:10d}".format(a)) # 10칸 만들기
print("{:010d}".format(a)) # 공란을 0으로 채우기
print("{:3d}".format(123456789)) # 공란보다 수가 커도 모두 출력
print("{:3,d}".format(123456789)) # 천단위 표시
print("{:.2f}".format(12.12345)) # 소숫점 2자리까지만 출력
print("{:.012f}".format(12.12345)) 
print("{:+010d}".format(a))

# 문자열 upper, lower : 영문자에만 적용
# upper: 영문자를 모두 대문자로, lower: 영문자를 모두 소문자로

cc = "aabbccddee"
print(cc.upper())

dd = "AABBCCDDEE"
print(dd.lower())

# # 문자열의 구조 파악하기
# # 문자인지 아닌지 확인
# # 이름을 입력받는데, 영문이름
# name = input("이름을 입력하세요.")
# if name.isalpha(): # 특수문자나 숫자인지 확인 가능
#     print("문자 알파벳으로 되어 있습니다.")
# else:
#     print("특수문자나 숫자가 입력되었습니다.")
# print(name)

# # 알아둘 것
# num = input("숫자를 입력하세요.>>>")
# if num.isdigit(): # 입력값이 숫자형 문자열인 경우만 숫자로 변경
#     num = int(num)
#     print("입력숫자:",num)
# else:
#     print(num)

# # 사람과 점수 출력
# num = input("이름입력:")
# kor = int(input("국어점수 입력:"))
# print(name,kor)

# # 입력이 잘못되는 경우 대비(에러발생)하여 입력이 바른 경우만 숫자로 변환
# num = input("이름입력:")
# kor = int(input("국어점수 입력:"))
# if kor.isdigit():
#     kor = int(kor)
# else:
#     print("숫자가 아닙니다. 다시 입력해주세요.")
# print(name,kor)

# # 입력이 잘못되는 경우 대비(에러발생) -> 다시 입력하게 하려면
# name = input("이름입력:")
# while(True):
#     kor = input("국어점수 입력:")
#     if kor.isdigit():
#         kor = int(kor)
#         break
#     else:
#         print("숫자가 아닙니다. 다시 입력해주세요.")

# print(name,kor)

# # while문 
# while(True): # 무한정 반복하라
#     id = input("아이디:")
#     pw = input("패스워드:")
#     if id=="aaa" and pw == "1111":
#         print("로그인성공! 메인페이지로 이동합니다")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인해주세요")
# print("메인페이지가 열립니다.")

# 횟수
paper = '''\
네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
이번 홍수의 원인으로 지목된 것처럼 
산 위의 빙하가 붕괴되면서 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다.\
'''

result1 = paper.find("홍수")
print(result1)

result2 = paper.rfind("홍수")
print(result2)

result3 = paper.count("홍수")
print(result3)

# 홍수라는 글자가 어디어디에 있는 지 위치점을 알고 싶어요.
result1 = paper.find("홍수") # 결과값은 4번자리
print(result1) 

result2 = paper.find("홍수",5) # 5번부터 찾아라
print(result2)

# find(검색내용, 시작위치, 종료위치) # 조건문, 반복문 등에서 자주 활용
