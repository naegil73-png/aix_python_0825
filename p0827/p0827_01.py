# 0826복습

# 학생 2명의 성적을 입력받아 출력하시오.
# 번호, 이름, 국어, 영어, 수학점수를 입력받아
# 번호, 이름, 국어, 영어, 수학, 합계, 평균을 출력하시오.
# 풀이 순서 : 성적입력, 성적계산, 성적출력

# # 성적입력
# num = input("번호 : ")
# name = input("이름 : ")
# kor = int(input("국어성적 : "))
# eng = int(input("영어성적 : "))
# math = int(input("수학성적 : "))
# # 성적계산
# total = kor+eng+math
# avg = total/3

# num2 = input("번호 : ")
# name2 = input("이름 : ")
# kor2 = int(input("국어성적 : "))
# eng2 = int(input("영어성적 : "))
# math2 = int(input("수학성적 : "))
# total2 = kor2+eng2+math2
# avg2 = total2/3

# # 성적출력
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(num, name, kor, eng, math, total, avg))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(num2, name2, kor2, eng2, math2, total2, avg2))
# # 같은 문자, 변수는 가급적 복사해서 붙여넣기(오타 발생 방지)


def record(num,name,kor,eng,math):
    num = num
    name = name
    kor = kor
    eng = eng
    math = math
    # 성적계산
    total = kor+eng+math
    avg = total/3
    print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(num, name, kor, eng, math, total, avg))
record(1,"홍길동",100,100,100)