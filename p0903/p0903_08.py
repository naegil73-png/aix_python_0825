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
    print(str,end="")
news.close()

# 인코딩 방식 - cp949 : 한글 ms에서만 가능, euc-kr : 국내 한글표준, utf-8: 국제 한글표준