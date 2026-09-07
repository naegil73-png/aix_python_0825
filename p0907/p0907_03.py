# # 파일 읽기
# readFile = open("C:\\aaa\\abc.txt",'r',encoding='utf-8')

# while True:
#     str = readFile.readline()
#     if str == 0: break
#     print(str,end="")

# readFile.close()
# print("프로그램 종료")

# # with로 파일 읽어오기 : close() 생략가능

# with open("C:\\aaa\\abc.txt",'r',encoding='utf-8') as f: # 파일에 한글과 영문이 혼합되어 있으면, encoding='utf-8'을 입력해야 함
#     while True:
#         str = f.readline()
#         if str == 0: break
#         print(str,end="")


# # stu.txt 출력
# stuList = []
# with open("C:\\aaa\\stu.txt",'r',encoding='utf-8') as f:
#     while True:
#         stu = f.readline() 
#         if stu == "": break
#         stu = stu.strip()
    
#         stu = stu.split(',')
#         for i,s in enumerate(stu):
#             if i == 0 or i == 1:continue
#             elif i >= 2 and i <= 5:
#                 stu[i] = int(s.strip()) # s[2]로 하면 100 중 0을 선택
#             elif i == 6:
#                 stu[i] = float(s.strip()) # 마지막줄도 항상 공백 제거

#         stuList.append(stu)

#     print(stuList)


# aaa.txt 출력

with open("C:\\aaa\\aaa.txt",'r',encoding='utf-8') as f:
    while True:
        str = f.readline()
        if str == '': break

        if str.strip().isdigit():
            str = int(str)

        print(type(str),end="")


# aaa.txt에서 내용을 전부 출력하되, 숫자는 합계를 구해서 맨 마지막 줄에 출력

sum = 0
with open("C:\\aaa\\aaa.txt",'r',encoding='utf-8') as f:
    while True:
        str = f.readline()
        if str == '': break

        if str.strip().isdigit():
            str = int(str)
            sum += str
    print(str,end="")
print("합계:",sum)

# # abc 출력

# with open("C:\\aaa\\aaa.txt",'r',encoding='utf-8') as f:
#     while True:
#         str = f.readline()
#         if str == 0: break
#         print(str,end="")