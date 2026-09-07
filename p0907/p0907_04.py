# common 폴더 안에 stu.tst로 파일을 저장하시오.
# 1
# 홍길동
# 100
# 100
# 100
# 300
# 100.0 

# with open("common\\stu.txt",'w',encoding='utf-8') as f:
#     allStr = ""
#     while True:
#         outStr = input("입력하시오:")
#         if outStr == "":
#             f.write(allStr+'\n')
#             break
#         allStr += (outStr+",")
#     print(allStr)

m_str = '"서울특별시  (1100000000)","9,330,658","4,482,949","          2.08","4,504,432","4,826,226","          0.93"'
test = m_str.split('","')
for i,t in enumerate(test):
    t = t.replace('"',"") # 맨 앞과 뒤의 "제거
    t = t.replace(",","") # 숫자 안의 , 제거(숫자안 ,는 문자)
    t = t.strip()
    if t.isdigit():
        t = float(t)
        test[i] = t
    print(type(t))
print(test)

# --------------------------------------------------------------------
# 서울 전체인구에서 남성비율은 몇 %인가?
print("서울총인구 대비 남성비율:{:.2f}%".format(test[4]/test[1]*100))