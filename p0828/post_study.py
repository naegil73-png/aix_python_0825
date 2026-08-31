'''
# 성적표를 리스트로 반환

s = []
s.append(input("번호:"))
s.append(input("이름"))
s.append(input("이름"))
s.append(input("이름"))
s.append(input("이름"))
'''


# 1~100까지 합계
total = 0
for i in range(1,101):
    total = i + total
print("합계:",total)

# 1~100까지 더할 때, 200을 넘을 때의 숫자와 그때까지의 합계
# 기획 : 1~100까지 더하는 구문, 200보다 넘는 지 조건문, 그 때의 숫자와 합계, 조건을 만족하면 중단하는 명령 

total = 0
for i in range(1,101):
    total = total + i
    if total >= 200:
        print("숫자:{}, 합계:{}".format(i,total))
        break

# 1~100까지 더할 때, 200을 넘기 직전의 숫자와 그때까지의 합계
# 기획 : 1~100까지 더하는 구문, 200보다 넘는 지 조건문, 그 때의 앞 숫자와 합계, 조건을 만족하면 중단하는 명령 

total = 0
for i in range(1,101):
    total = total + i
    if total >= 200:
        print("숫자:{}, 합계:{}".format(i-1,total-i))
        break

# 구구단을 구문을 작성, 단, 구단간에는 한줄씩 띄울 것

for i in range(2,10):
    for j in range(1,10):
        print(i,'X',j,'=',i*j)
    print()
# for문을 이용하여, 여러 사람의 이름과 성적을 입력받아 입력내용과 합계, 평균을 출력하는 명령 구문 작성
# 구문기획 : for문, 입력 -> input, 합계, 평균의 계산 -> 숫자형은 int로 변환

'''
for i in range(1,3):
    name = input("이름:")
    kor = int(input("국어:"))
    eng = int(input("영어:"))
    total = kor+eng
    avg = total/3

for i in range(1,3):
    print("{}\t{}\t{}\t{}\t{}".format(name,kor,eng,total,avg)) # 마지막 입력만 반복됨
'''
    
# 리스트로 전환하여 for문을 이용하여, 여러 사람의 이름과 성적을 입력받아 입력내용과 합계, 평균을 출력하는 명령 구문 작성
# 구문기획 : for문, 입력 -> input, 합계, 평균의 계산 -> 숫자형은 int로 변환, list에 추가

name = []
kor = []
eng = []
total = []
avg = []
stu = []
for i in range(2):
    name.append(input("이름:"))
    kor.append(int(input("국어:")))
    eng.append(int(input("영어:")))
    total.append((kor+eng))
    stu.append([name,kor,eng,total,avg])
for i in range(2):
    print("{}\t{}\t{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2],stu[i][3],stu[i][4]))

    # 프로그램의 민감한 부분은 AI에 돌리면 안됨

    