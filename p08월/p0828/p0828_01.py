# 1. 번호, 이름, 국어, 영어, 수학 입력
# 2. 합계, 평균을 계산
# 3. 성적 출력하도록 구성하시오

# 입력은 변수에 저장해야 함. 계속 사용하려면 DB에 저장해야 함(추후 진행예정)
no = input("번호입력:")
name = input("이름입력:")
kor = int(input("국어점수:")) # input만 하고, 다음줄에 kor = int(kor) 로 해도 됨
eng = int(input("영어점수:"))
math = int(input("수학점수:"))
total = kor+eng+math
avg = total/3 # 나눗셈하면 float 자료형으로 바뀜

# 이렇게 하면, 학생이 많아질 경우, 입력 변수가 너무 많아짐.(100명이면, 700개의 변수에 입력해야 함)
# 이런 문제를 해결하기 위해 리스트를 활용, 딕셔너리도 마찬가지..
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no,name,kor,eng,math,total,avg))
print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}") # 이렇게 표현 가능

# 리스트에 저장
s = []
no = input("번호입력:")
name = input("이름입력:")
kor = int(input("국어점수:")) # input만 하고, 다음줄에 kor = int(kor) 로 해도 됨
eng = int(input("영어점수:"))
math = int(input("수학점수:"))
total = kor+eng+math
avg = total/3 # 나눗셈하면 float 자료형으로 바뀜
s.append(no)

# 이렇게 하면, 학생이 많아질 경우, 입력 변수가 너무 많아짐.(100명이면, 700개의 변수에 입력해야 함)
# 이런 문제를 해결하기 위해 리스트를 활용, 딕셔너리도 마찬가지..
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no,name,kor,eng,math,total,avg))
print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}") # 이렇게 표현 가능