# import os 
# print("운영체제:",os.name)
# print("현재 폴더:",os.getcwd()) # 현재 작업 중인 폴더
# print("현재 폴더안 요소:",os.listdir()) # 현재 작업 중인 폴더 요소

# # os.mkdir("abc") # 현재 폴더에 폴더를 만들기

# news = open("new.txt","r")
# while True:
#     str = news.readline() # 1줄씩 읽어오기
#     if str == "": break # "" - 빈공백, 즉 빈공백이면, break
#     print(str,end=" ")
# news.close()

news = open("new1.txt","r",encoding="utf-8")
while True:
    str = news.readline() # 1줄씩 읽어오기
    if str == "": break # "" - 빈공백, 즉 빈공백이면, break
    print(str,end="") # 파일에 줄바꿈(\n)이 있기 때문에 print에 있는 줄바꿈을 ""로 변경
news.close()

# 인코딩 방식 - cp949 : 한글 ms에서만 가능, euc-kr : 국내 한글표준, utf-8: 국제 한글표준

# 만약, 다른 위치의 파일을 불러올 경우
news = open("C:/down/aaa.txt",'r')
while True:
    str1 = news.readline()
    if str1 == "": break
    print(str1,end="")
print()

import time
print(1)
print(2)
print(3)
print(4)
time.sleep(3) # 4까지 실행하다가 3초간 대기하게 됨
print(5)
print(6)
print(7)

# 학생성적과 05.py 보고 있을 것