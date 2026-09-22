# with open("C:\\aaa\\a.txt",'w',encoding='utf-8') as f:
#     while True:
#         outstr = input("내용입력")
#         if outstr == "": break
#         f.write(outstr+'\n')

# print("파일내용이 저장되었습니다.")

# with open("C:\\aaa\\a.txt",'a',encoding='utf-8') as f:
#     while True:
#         outstr = input("내용입력")
#         if outstr == "": break
#         f.write(outstr+'\n')

# print("파일내용이 추가되었습니다.")

# # 없는 폴더에 파일 저장 시 에러
# with open("C:\\aaa2\\a.txt",'2',encoding='utf-8') as f:
#     while True:
#         outstr = input("내용입력")
#         if outstr == "": break
#         f.write(outstr+'\n')

# print("파일내용이 추가되었습니다.")

# # 없는 폴더에 저장하면 에러 발생하므로 있는 지 없는 지를 확인하고 폴더를 생성하는 작업
# import os
# if not os.path.exists("C:\\aaa2"): # aaa2폴더가 없다면..
#     os.makedirs("C:\\aaa2") # aaa2폴더를 생성해줌

# with open("C:\\aaa2\\a.txt",'a',encoding='utf-8') as f:
#     while True:
#         outstr = input("내용입력")
#         if outstr == "": break
#         f.write(outstr+'\n')

# print("파일내용이 추가되었습니다.")

# # 
# if not os.path.exists("C:\\aaa3"): # aaa2폴더가 없다면..
#     os.makedirs("C:\\aaa3") # aaa2폴더를 생성해줌
# with open("C:\\aaa3\\a.txt",'a') as f:
#     while True:
#         outStr = input("내용입력:")

import os
frame = input("저장할 파일이름을 입력하세요(파일명):") # 폴더/파일명 또는 파일명만 입력할 수도 있음

if not os.path.exists('C:\\common'): # C:\\common 경로가 없다면,
    os.makedirs("C:\\common") # C:\\common 경로를 만들어라

with open("C:\\common\\"+frame,"a",encoding='utf-8') as f: # 만들어진 경로에 파일을 만들어라(a도 만들기 가능)
    while True:
        outStr = input("내용입력:")
        if outStr == "":break
        f.write(outStr+'\n')
