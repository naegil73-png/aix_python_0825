# read(): 바이트 단위 읽음
# readline(): 한줄 읽기 # 양이 많으면 사용하는 게 나을 수도...
# readlines(): 모두 읽기

file1 = open("C:\\aaa\\test1.txt",'r',encoding='utf-8') # txt읽을 때, utf-8로 저장, 읽어야 함. 1번째 작성
# 3줄을 읽으려고 함 # 3번째 작성
f1 = file1.readline()
print(f1,end="")
f2 = file1.readline()
print(f2,end="")
f3 = file1.readline()
print(f3,end="")
file1.close() # 2번째 작성

# 있는 대로 다 읽기
f = open("C:\\aaa\\test1.txt",'r',encoding='utf-8')
while True:
    line = f.readline()
    if not line:break # 줄을 다 읽었다면..
    print(line,end="")
f.close()