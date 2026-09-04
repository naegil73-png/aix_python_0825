# test2.txt파일을 읽어와서 
# stu = []
# 데이터를 리스트에 저장하시오.

stu = []
with open("C:\\aaa\\test2.txt",'r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        line = line.strip()
        if line == "": break
        line1 = line.split(",")
        
        print(line1,end="")

        for i,v in enumerate(line1):
            if 2<=i<5:
                line[i] = 

        stu.append(line)

    print(stu)
