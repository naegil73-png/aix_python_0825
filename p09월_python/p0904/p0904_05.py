f = open("C:\\aaa\\test2.txt",'r',encoding='utf-8')
while True:
    s = f.readline()
    if not s:break
    print(s,end="")
f.close()

# 1,홍길동,100,100,100,300,100.0
# 2,유관순,100,100,100,300,100.0
# 3,이순신,100,100,100,300,100.0 결과를 , 기준으로 분리

f = open("C:\\aaa\\test2.txt",'r',encoding='utf-8')
while True:
    line = f.readline()
    arr = line.split(",")
    if not line:break
    print(arr)
    print(line,end="")
f.close()

# 문자형 숫자를 숫자로 전환
f = open("C:\\aaa\\test2.txt",'r',encoding='utf-8')
while True:
    line = f.readline()
    arr = line.split(",")
    for i, a in enumerate(arr):
        if 5 >= i >= 2:
            arr[i] = int(a)
        if i == 6:
            arr[i] = float(a)
    if not line:break
    print(arr)
    print(line,end="")
f.close()

# stu리스트에 저장

stu=[]
f = open("C:\\aaa\\test2.txt",'r',encoding='utf-8')

while True:
    line = f.readline() # 1,홍길동,100,100,100,300,100.0 \n
    if line == "":break # 
    line = line.strip() # 줄바꿈 에러 제거 -> 1,홍길동,100,100,100,300,100.0
    print(line,end="")

    arr = line.split(",") # list로 변환

    for i, a in enumerate(arr): 
        if 5 >= i >= 2: # 3~6번째까지 정수로 변환
            arr[i] = int(a)
        elif i == 6: # 7번째는 실수로 변환
            arr[i] = float(a)
    stu.append({'no':arr[0],"name":arr[1],"kor":arr[2],"eng":arr[3],'math':arr[4],"total":arr[5],"avg":arr[6]})
    print(arr)
f.close()
print(stu)

# 확인 : 파일 읽어오기
stu = []
f = open("C:/aaa/test2.txt","r",encoding="utf-8")
while True:
    line = f.readline() # /n 줄바꿈때문에 에러가 남.
    if line=="": break
    line = line.strip()

    print(line,end="")
    arr = line.split(",")

    for i,a in enumerate(arr):
        if 5>=i>=2:
            arr[i] = int(a)
        elif i==6:
            arr[i] = float(a)
    # stu 리스트에 저장
    # print(arr)
    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})


f.close()
print(stu)

# 

stu = []
f = open("C:/aaa/test2.txt","r",encoding="utf-8")
while True:
    line = f.readline() # /n 줄바꿈때문에 에러가 남.
    if line=="": break
    line = line.strip()

    print(line,end="")
    arr = line.split(",")

    for i,a in enumerate(arr):
        if 5>=i>=2:
            arr[i] = int(a)
        elif i==6:
            arr[i] = float(a)
    # stu 리스트에 저장
    # print(arr)
    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})


f.close()
print(stu)