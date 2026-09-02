# # 번호, 이름, 국어, 영어, 수학을 입력받아
# # 번호, 이름, 국어, 영어, 수학, 합계, 평균을 출력하시오. 평균은 소숫점 둘째자리까지 표시
# # 결과 : 1 홍길동 100 100 100 300 100.0

# num = input("번호 : ")
# name = input("이름 : ")
# kor = int(input("국어점수 : "))
# eng = int(input("영어점수 : "))
# math = int(input("수학점수 : "))
# total = kor+eng+math
# avg = total/3

# print("{} {} {} {} {} {} {:.2f}".format(num,name,kor,eng,math,total,avg))

# 이렇게 출력하기
'''
------------------------------------------------------------
번호    이름    국어    영어    수학    합계    평균
1       홍길동  100     100     99      299     99.67
2       유관순  100     100     98      298     99.33
------------------------------------------------------------
'''

'''
num = input("번호 : ")
name = input("이름 : ")
kor = int(input("국어점수 : "))
eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))
total = kor+eng+math
avg = total/3


num2 = input("번호 : ")
name2 = input("이름 : ")
kor2 = int(input("국어점수 : "))
eng2 = int(input("영어점수 : "))
math2 = int(input("수학점수 : "))
total2 = kor2+eng2+math2
avg2 = total2/3

print("-"*60)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(num,name,kor,eng,math,total,avg))
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(num2,name2,kor2,eng2,math2,total2,avg2))
print("-"*60)

'''

# # id = aaa, pw = 1111 이 맞는 지 확인하는 구문 작성

# id = input("아이디 : ")
# pw = input("패스워드 : ")

# print("아이디 확인 : {}".format('aaa' == id))
# print("패스워드 확인 : {}".format('1111'==pw))

# # 홀짝 확인
# a = 7
# print(a%2==1)

# if a%2 == 1:
#     print("{}는 홀수입니다".format(a))
# else:
#     print("{}는 짝수입니다".format(a))

# # id = aaa, pw = 1111로 입력되면, 로그인되었습니다. 아니면, 아이디와 패스워드를 확인해 주세요를 출력

# id = input("아이디 : ")
# pw = input("패스워드 : ")

# if (id == 'aaa') and (pw == '1111'):
#     print("로그인되었습니다.")
# else:
#     print("아이디와 패스워드를 확인해 주세요.")

print("# 연습문제")
print("\\\\\\\\") # \출력은 \\로 해야함. 따라서 홀수는 에러 발생
print("-"*8)

# 5 + 7 = 12를 출력
print("5 + 7 =",5+7) 
print("5 + 7 = {}".format(5+7))
print(5,"+",7,"=",5+7)

# print는 여러 인자를 동시에 받을 수 있음. 문자열은 변수 지정 또는 "", '', ''' ''' 인 경우 외에는 ,를 쓸 수 없음
# 따옴표 밖의 ,는 코드를 나누는 문법 기호이므로 hello, world로 표시되었다면 에러 발생, "hello", "world"라고만 쓰면 튜플로 인식