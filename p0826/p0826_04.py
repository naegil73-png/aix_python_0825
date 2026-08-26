# 송금금액 : 100 입력 받고
# 현 잔액 : 1000
# 총금액을 출력하시오.

# total1 = 1000
# send = int(input("송금금액을 입력하세요. : "))
# total2 = total1+send

# print("잔액 : {}, 송금금액 : {}, 총금액 : {}".format(total1, send, total2))

# print("잔액 : ",total1) # 이렇게로도 출력 가능
# print("송금금액 : ",send) # 이렇게로도 출력 가능
# print("총금액 : ",total2) # 이렇게로도 출력 가능

# 국어, 영어, 수학점수를 입력받아
# 합계, 평균을 출력하시오.
# 합계: 300, 평균 : 100

kor = int(input("국어점수를 입력하세요 : "))
eng = int(input("영어점수를 입력하세요 : "))
mat = int(input("수학점수를 입력하세요 : "))
total = kor+eng+mat
avg = total/3

print("세과목 점수 합계는 {}, 평균은 {}". format(total, avg))