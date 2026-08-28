print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
# 1을 다섯번 출력하는 데 5문장 필요 -> 반복문으로 단축필요
# 반복문 : ************ for 변수 in 범위:
for i in range(10): # for는 한바퀴 돌 때마다 다음 것으로 자동 진행
    print(2)
for i in range(10):
    print(i)

for i in range(5):
    print(i*10)

for i in range(1,6):
    print(i)

for i in range(7,12):
    print(i)

# 두칸씩 띄어서 출력
for i in range(7,12,2): # 
    print(i)

for i in [1,5,3,2]: # 
    print(i)

for i in "안녕하세요":
    print(i)

# range사용 : arr = list(range(11))

for i in range(10):
    print("안녕")

for _ in range(10): # 이렇게 써도 됨
    print("안녕")

# for i in range(3):
#     print("번호:",i+1)
#     name = input("이름 입력:")
#     print(name)

# 성적표 적용

# for i in range(2):
#     print("번호:", i+1, end = "\t")
#     name = input("이름 입력:")
#     kor = int(input("국어점수:"))
#     print("{} {}".format(name,kor))


# for i in range(3):
#     no = i+1
#     name = input("이름 입력:")
#     kor = int(input("국어점수:"))
#     print("{} {} {}".format(no, name,kor))

# 1부터 10까지 더하기
sum = 0
for i in range(1,11):
    sum += i
print("합계:",sum)

# 1부터 100까지 더하기 ******** 합하기 공식임
sum = 0
for i in range(1,101):
    sum = sum + i
print("합계 : {}".format(sum))

# 합계가 100이 넘어가는 시점은 숫자가 얼마일까?
# 그리고 100을 넘기기 이전의 숫자와 그 때까지의 합계
sum = 0
for i in range(1,101):
    sum += i
    if sum > 100:
        print("100보다 클 때:",i)
        break
print("합계", sum)
print("{}번까지 합: {}".format(i-1, sum-i))

# 10까지 숫자에서 합계가 11을 넘어갈 때의 숫자와 합계, 그리고 직전의 숫자와 합계
sum = 0
for i in range(1,11):
    sum += i
    if sum > 11:
        print("11보다 클 때:",i)
        break
print("합계", sum)
print("{}번까지 합: {}".format(i-1, sum-i))

# 파이썬 튜터로 학습 가능
# ctrl + \로 해도 참조설정 안되면, 아래의 한컴입력기 -> 마이크로소프트 입력기로 변환시켜야 함

for i in range(1,10):
    print("2 X {} = {}".format(i,i*2))

# for문 안에 for문을 쓸 수 있음
# 구구단
for i in range(2,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))

for i in range(1,4):
    for j in range(1,4):
        print(i,j)

# 3번 곱하기        
num = 0
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            num += 1
            print(num,"번째 계산")
            print("{} X {} X {} = {}".format(i,j,k,i*j*k))
