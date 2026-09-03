my_info = {"id":'aaa',"pw":1111,'money':10_000_000, 'bonusPoint':0}
product = [
    {"p_name":"컴퓨터", 'price':1000000, 'bonusPoint':1000000*0.1},
    {"p_name":"냉장고", 'price':2000000, 'bonusPoint':2000000*0.1},
    {"p_name":"오디오", 'price':500000, 'bonusPoint':500000*0.1}

]
cart = []

while True:
    print('[온라인 쇼핑몰에 오신 것을 환영합니다.]')
    id = input("아이디:")
    pw = input("패스워드")
    if id == my_info['id'] and pw == my_info["pw"]:
        print("로그인되었습니다.")
        break
    else:
        print("아이디 또는 패스워드를 확인해 주세요.")

    print("현재금액:",my_info['money'])
    print("보너스포인트:",my_info['bonusPoint'])

    while True:
        print()
        print("쇼핑몰 구매 목록")
        for i, p in enumerate(product):
            print(f"{i+1}.{p['p_name']}:{p['price'],p['bonusPoint']}")
        choice = int(input("제품선택:"))
        if choice == 1:
            buy1 = input("냉장고를 구매하시겠습니까?(1번: 구매, 0번: 취소):")
            if buy1 == 1:
                print("구매가 완료되었습니다.")
                my_info['money'] -= product[0][1]



    print('[1.컴퓨터, ]')
    print('[온라인 쇼핑몰에 오신 것을 환영합니다.]')
    print('[온라인 쇼핑몰에 오신 것을 환영합니다.]')
