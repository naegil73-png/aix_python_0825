# 반복문을 사용해서 1~100까지 합을 출력하시오.
# 200을 넘는 시점의 수와 그때까지의 합계를 출력하시오.
# 200을 넘기 직전 시점의 수와 그 때까지의 합계를 출력하시오.
# 구구단을 출력하시오.

# 100까지 합계
total = 0
for i in range(1,101):
    total = total + i
print("합계", total)

# 200을 넘는 시점의 수와 그 때까지의 합
total = 0
for i in range(1,100):
    total = total + i
    if total > 200:
        print("200이 넘을 때의 수: ",i,"그때까지 합계:",total)
        break # 조건이 만족되면 if문을 중단한다.

# 200을 넘기 이전 시점의 수와 그 때까지의 합
print("200넘기 직전 수:",i-1,"그때까지 합계:",total-i)

# 구구단

for i in range(2,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))

# 여러사람의 성적, 정보를 입력
# for문으로 실행

name = []
kor = []
for i in range(2):
    name.append(input("이름입력:"))
    kor.append(input("국어성적:"))

for i in range(2):
    print("{}\t{}".format(name[i],kor[i]))

name = []
kor = []
stu = []
for i in range(2):
    name.append(input("이름입력:"))
    kor.append(input("국어성적:"))
    stu.append([name,kor]) # 리스트 안에 다시 리스트로 추가
for i in range(2): # 없으면, 한줄씩 출력. 있어야 위의 구문이 전체 수행되고 한꺼번에 출력됨
    print("{}\t{}".format(name[i],kor[i]))

no = []    
name = []
kor = []
stu = []
for i in range(2):
    no = i+1
    name.append(input("이름입력:"))
    kor.append(input("국어성적:"))
    stu.append([no,name,kor]) # 리스트 안에 다시 리스트로 추가
for i in range(2):
    print("{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2]))