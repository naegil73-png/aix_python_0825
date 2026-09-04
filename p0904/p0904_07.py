# # 파일 만들기, 덮어쓰기

# with open("C:\\aaa\\abc.txt",'w',encoding='utf-8') as f:
#     while True:
#         line = input("글을 입력하세요.>>")
#         if line != "":
#             f.writelines(line+"\r\n") # \r: 문장 끝으로, \n: 줄바꿈 (문장끝으로 가서 줄바꿈하라)
#         else: # 빈공백(엔터키 등)
#             break
# print("파일이 저장되었습니다.")

# 이어쓰기 : 내용추가 하기

with open("C:\\aaa\\abc.txt",'a',encoding='utf-8') as f:
    while True:
        line = input("글을 입력하세요.>>")
        if line != "":
            f.writelines(line+"\r\n") # \r: 문장 끝으로, \n: 줄바꿈 (문장끝으로 가서 줄바꿈하라)
        else: # 빈공백(엔터키 등)
            break
print("파일이 저장되었습니다.")