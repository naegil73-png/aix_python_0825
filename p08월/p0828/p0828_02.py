# 리스트에 저장
s = []

s.append(input("번호입력:"))
s.append(input("이름입력:"))
s.append(int(input("국어점수:")))
s.append(int(input("영어점수:")))
s.append(int(input("수학점수:")))
total = s[2]+s[3]+s[4]
avg = total/3
s.append(total)
s.append(avg)

# 이렇게 하면, 학생이 많아질 경우, 입력 변수가 너무 많아짐.(100명이면, 700개의 변수에 입력해야 함)
# 이런 문제를 해결하기 위해 리스트를 활용, 딕셔너리도 마찬가지..
print(s)

# 다른 방법
s = [0,0,0,0,0,0,0]
no = input("번호입력:")
name = input("이름입력:")
kor = int(input("국어점수:")) # input만 하고, 다음줄에 kor = int(kor) 로 해도 됨
eng = int(input("영어점수:"))
math = int(input("수학점수:"))
total = kor+eng+math
avg = total/3 # 나눗셈하면 float 자료형으로 바뀜
s[0]=input("번호입력:")
s[1]=input("이름입력:")
s[2]=int(input("국어점수:"))
s[3]=int(input("영어점수:"))
s[4]=int(input("수학점수:"))
s[5]=s[1]+s[2]+s[3]
s[6]=s[5]/3

# 이렇게 하면, 학생이 많아질 경우, 입력 변수가 너무 많아짐.(100명이면, 700개의 변수에 입력해야 함)
# 이런 문제를 해결하기 위해 리스트를 활용, 딕셔너리도 마찬가지..
print(s)

