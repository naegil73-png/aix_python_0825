# 송금금액 : 100 입력 받고
# 현 잔액 : 1000
# 총금액을 출력하시오.

total1 = 1000
send = int(input("송금금액을 입력하세요. : "))
total2 = total1+send
print("잔액 : {}, 송금금액 : {}, 총금액 : {}".format(total1, send, total2))

print("잔액 : ",total1) # 이렇게로도 출력 가능
print("송금금액 : ",send) # 이렇게로도 출력 가능
print("총금액 : ",total2) # 이렇게로도 출력 가능
