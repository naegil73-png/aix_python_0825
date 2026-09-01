aa = []
bb = []
value = 0
for i in range(0,100):
    aa.append(value)
    value += 2
print(aa)

for i in range(0,100):
    bb.append(aa[99-i])
print(bb)

cc = list(range(0,200,2))
print(cc)

dd = [i+2 for i in range(0,200,2)]
print(dd)

dd1 = [i for i in range(0,200,2)]
print(dd1)

aa = [10,20,30]
print(aa*3) # 리스트의 반복

aa = [1,2,3]
bb = [4,5,6]
print(aa+bb) # 리스트의 연결(extend와 같은 기능)
aa.extend(bb) # 위와 같으나 원본이 변경됨(aa)
print(aa)

a = 1
b = 2
print(a+b)

aa.append(1)
print(a)

# 원본이 변경되는 함수 : append, insert, del, pop, del
aa = [1,2,3,4,5,6,7]
print(aa[::-1]) # 역순정렬
print(aa[::-2]) # 역순정렬인데, 2씩 뛰어서..

aa = [10,20,30]
aa[1:2] = [200,201] # 2번째 자리에 2개의 원소로 교체
print(aa)

aa = [1,2,3]
aa[1:2] = [20,30] # 2번째 자리에 두개의 원소로 교체
print(aa)

aa = [1,2,3,4,5]
aa[1:4] = []
print(aa)

# 아래의 리스트를 수정하려고 한다면, 홍길동 -> 홍길자
stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0],
]
stu_list[0][1] = "홍길자"
print(stu_list)
print(stu_list[0][2:5]) # 리스트 형태로 출력
print(stu_list[0][2],stu_list[0][3],stu_list[0][4]) # 숫자형태로 출력

# 유관순 - 국어:100, 영어:50 으로 수정후 출력

stu_list[1][2:4] = (100, 50) 
print(stu_list)

stu_list[1][2] = 100 
stu_list[1][3] = 50 
print(stu_list)
# 합계, 평균은 그대로 있음 -> 수정 필요

stu_list[1][5] = stu_list[1][2]+stu_list[1][3]+stu_list[1][4]
stu_list[1][6] = stu_list[1][5]/3
print(stu_list)

# 리스트 안에 검색한 이름이 있는 지 찾는 문구
name_arr = ["홍길동","유관순","이순신","강감찬","김구"]

while True:
    name = input("검색할 이름을 입력하세요.>>")
    if name in name_arr:
        print(name," 학생이 검색되었습니다.")
        break
    else:
        print(name," 학생은 없습니다.")

# 리스트 안에 검색한 이름이 있는 지 찾아서 변경하는 문구
name_arr = ["홍길동","유관순","이순신","강감찬","김구"]

while True:
    name = input("검색할 이름을 입력하세요.>>")
    if name in name_arr:
        no = name_arr.index(name)
        print(name," 학생이 검색되었습니다.")
        break
    else:
        print(name," 학생은 없습니다.")

# 없으면 없다는 문구 표시
stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0],
]
while True:
    name = input("검색이름입력:")
    for stu in stu_list:
        if name in stu:
            print("있음")
        else:
            print("해당하는 이름이 없습니다.")

    break

# 리스트에 없는 경우에만 없다는 문구 한번 표시
stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0],
]
while True:
    name = input("검색이름입력:")
    flag = 0
    for stu in stu_list:
        if name in stu:
            print("있음")
            flag = 1
            break
    if flag == 0:
        print("해당하는 이름이 없습니다.")
    break

# 리스트에 없는 경우에만 없다는 문구 한번 표시, 인덱스 표시
stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0],
]
while True:
    name = input("검색이름입력:")
    flag = 0
    for i, stu in enumerate(stu_list):
        if name in stu:
            stu_index = i
            print("있음")
            flag = 1
            break
    if flag == 0:
        print("해당하는 이름이 없습니다.")
    break