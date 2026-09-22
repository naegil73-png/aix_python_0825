# 로또 맞추기
# 학생성적 프로그램
# 학생성적입력 - 변수, 리스트 - 리스트, 리스트 -딕셔너리

# [1,2,3,4,5,6,7,8,9] 1차원 리스트
# 작성방법 - 직접입력, [0]*10, list(range(1,10))
num_arr = list(range(1,10))
print(num_arr)

# 0~9까지 수 중 0,3,6,9를 선택하여 추가한 리스트로 반환
all_arr = []
for i in range(0,9,3):
    all_arr.append(num_arr[0:3]) # 0,1,2
    all_arr.append(num_arr[3:6]) # 3,4,5
    all_arr.append(num_arr[6:9]) # 6,7,8

# 이렇게 사용할 수 있음    
# all_arr = []
# for i in range(0,9,3):
#     all_arr.append(num_arr[i:i+3]) # 첫번째는 i=0 입력되어 [0:3], 두번째는 for문에서 i=3 입력되어 [3:6]...

# stu_list = [
#     [1,"홍길동",100,100,100,300,100.0]
#     [2,"유관순",100,100,100,300,100.0]
#     [3,"이순신",100,100,100,300,100.0]
# ]
# # 이런 형태로 만들려고 함

# stu_list = []
# stu_list.append([1,"홍길동",100,100,100,300,100.0])
# stu_list.append([2,"유관순",100,100,100,300,100.0])
# stu_list.append([3,"이순신",100,100,100,300,100.0])

# # stu_list = []
# # no = input("번호입력:")
# # name = input("이름입력:")
# # kor = int(input("국어입력:"))
# # eng = int(input("영어입력:"))
# # math = int(input("수학입력:"))
# # total = kor+eng+math
# # avg = total/3
# # stu_list.append([no,name,kor,eng,math,total,avg]) # 이런 형태로 입력 -> for문으로 입력

# stu_list = []
# for i in range(3):
#     no = input("번호입력:")
#     name = input("이름입력:")
#     kor = int(input("국어입력:"))
#     eng = int(input("영어입력:"))
#     math = int(input("수학입력:"))
#     total = kor+eng+math
#     avg = total/3
#     stu_list.append([no,name,kor,eng,math,total,avg])
# for i in range(3):pass
# print(stu_list)

# 반복문을 중간에 나오고 싶다면.. 번호 처리에서 삭제, 추가해도 반영이 되도록 하는 방법(count 이용)
stu_list = []
while True: # 무한정 반복하라.
    no = len(stu_list)+1 # 
    print("자동번호:",no)
    name = input("이름입력:")
    if name == "0":break
    kor = int(input("국어입력:"))
    eng = int(input("영어입력:"))
    math = int(input("수학입력:"))
    total = kor+eng+math
    avg = total/3
    stu_list.append([no,name,kor,eng,math,total,avg])
    
# ******* 전개연산자
print("입력된 학생성적:", len(stu_list))
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)
for s in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s)) # *는 전개 연산자(p0901_05.py에서 설명) - 각 요소를 분리해서 각각 적용해줌