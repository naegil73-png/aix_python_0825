my_info = [
    {"id":"aaa","pw":1111,"money":10000000,"bonuspoint":0}
]
product = [
    {"p_name":"컴퓨터","price":1000000,"bonuspoint":100000},
    {"p_name":"냉장고","price":2000000,"bonuspoint":100000},
    {"p_name":"오디오","price":500000,"bonuspoint":100000}
]

while True:
    id = input("아이디:")
    pw = int(input("패스워드:"))
    if id == "aaa" and pw == 1111:
        print("로그인이 완료되었습니다.")
        break
    else:
        print("아이디 또는 패스워드가 일치하지 않습니다.")

while True:
    print("[쇼핑몰 구매목록]")
    for i,v in enumerate(product):
        print(f"{i+1}.{v['p_name']}:{v['price']},{v['bonuspoint']}")
    choice = int(input("어떤 제품을 구입하시겠습니까?(0:구매 중지)"))
    if choice == 1:
        choice1 = int(input("냉장고 구매하시겠습니까?(1:구매,0:취소)"))
        if choice1 == 1:
            print(f"{product[choice1-1]['p_name']}", "을 구매해 주셔서 감사합니다.")
            spend = int(product[choice-1]['price'])
            print(f"{spend}","가 지출되었습니다.")
            my_info['money'] -= spend
            print("잔고에", f"{my_info['money']}")
























# # 0903_04 보고 함수로 작성

# my_info = {"id":'aaa',"pw":1111,'money':10_000_000, 'bonusPoint':0}
# product = [
#     {"p_name":"컴퓨터", 'price':1000000, 'bonusPoint':1000000*0.1},
#     {"p_name":"냉장고", 'price':2000000, 'bonusPoint':2000000*0.1},
#     {"p_name":"오디오", 'price':500000, 'bonusPoint':500000*0.1}

# ]
# cart = []

# while True:
#     print('[온라인 쇼핑몰에 오신 것을 환영합니다.]')
#     id = input("아이디:")
#     pw = input("패스워드")
#     if id == my_info['id'] and pw == my_info["pw"]:
#         print("로그인되었습니다.")
#         break
#     else:
#         print("아이디 또는 패스워드를 확인해 주세요.")

#     print("현재금액:",my_info['money'])
#     print("보너스포인트:",my_info['bonusPoint'])

#     while True:
#         print()
#         print("쇼핑몰 구매 목록")
#         for i, p in enumerate(product):
#             print(f"{i+1}.{p['p_name']}:{p['price'],p['bonusPoint']}")
#         choice = int(input("제품선택:"))
#         if choice == 1:
#             buy1 = input("냉장고를 구매하시겠습니까?(1번: 구매, 0번: 취소):")
#             if buy1 == 1:
#                 print("구매가 완료되었습니다.")
#                 my_info['money'] -= product[0][1]



#     print('[1.컴퓨터, ]')
#     print('[온라인 쇼핑몰에 오신 것을 환영합니다.]')
#     print('[온라인 쇼핑몰에 오신 것을 환영합니다.]')



# # 두 수를 함수의 매개변수로 입력받아 사칙연산하는 구문


# # 함수로 1.컴퓨터 1000000, 2.세탁기 2000000, 3.오디오 500000 을 항상 표출, 입력은 제품번호/수량 형태로 하고, 제품 선택 시 선택사항과 총 구매금액을 출력
# # 1/3 : 1번 3개 구매함을 의미
# # 총 구매금액을 출력하시오.

# # # 두 숫자를 n1/n2 형태로 입력하고, 앞 자리 숫자에는 10, 뒷 자리 숫자에는 100을 곱한 후 합계를 구할 것

# # 함수 이용, 1번 구구단, 2번 두수 입력받아 사칙연산, 3번 1~10까지 합산하는 함수

# # 반올림, 올림, 내림 함수로 10.3을 출력

