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

