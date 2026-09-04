# test2.txt파일을 읽어와서 
# stu = []
# 데이터를 리스트에 저장하시오.

stu = []
with open("C:\\aaa\\test2.txt",'r',encoding='utf-8') as f:
    while True:
        line = f.readline() # 한줄씩 읽어라
        line = line.strip() # 줄 앞뒤 공백 제거(엔터키)
        if line == "": break # 내용이 없는 줄이 있으면, break
        line1 = line.split(",")

        for i, v in enumerate(line1):
            if 2<=i<=5:
                line1[i] = int(v)
            elif i == 6:
                line1[i] == float(v)
        stu.append({"no":line1[0],"name":line1[1],"kor":line1[2],"eng":line1[3],"math":line1[4],"total":line1[5],"avg":line1[6]})

    print(stu)



