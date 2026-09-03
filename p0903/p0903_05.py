# s_arr = ["컴퓨터","냉장고","오디오","세탁기"]

# while True:
#     print("1.컴퓨터")
#     print("2.냉장고")
#     print("3.오디오")
#     print("4.세탁기")
#     choice = int(input("원하는 번호를 입력하세요>>"))
#     if choice == 1:
#         print("컴퓨터")
#         print("가격 : 100만원")
#     elif choice == 2:
#         print("냉장고")
#         print("가격 : 100만원")
#     elif choice == 3:
#         print("오디오")
#         print("가격 : 100만원")
#     elif choice == 4:
#         print("세탁기")
#         print("가격 : 100만원")
#     else:break

# my_info - id:aaa, pw:1111, money:10000000,bonuspoint:0 으로 
# product - 제품명: 컴퓨터, 가격:100만, 제품: 냉장고, 가격 : 200만, 제품:오디오, 가격:50만, 제품:세탁기, 가격:150만 을 구매해서 구매금액, 잔액 출력
# 잔액이 부족한 경우, 부족하다는 문구 표시

# 제품이 많은 경우, 위 구문을 줄인다면..
my_info = {"id":"aaa","pw":"1111",\
        "money":10_000_000,\
            "bonusPoint":0}
s_arr = [{"prd_name":"컴퓨터","price":1000000},
        {"prd_name":"냉장고","price":2000000},
        {"prd_name":"오디오","price":500000},
        {"prd_name":"세탁기","price":1500000}] # 항목을 파악을 용이하기 위해서 딕셔너리로 하는 것이 용이

def p_cal(choice):
    if my_info['money'] < s_arr[choice-1]['price']:
        print("잔액이 부족합니다.")
    print(f"구매상품: {s_arr[choice-1]['prd_name']}")
    print(f"가격: {s_arr[choice-1]['price']}원")
    my_info['money'] -= s_arr[choice-1]['price']
    print(f"상품구매 후 보유금액: {my_info['money']-s_arr[choice]['price']}")

while True:
    for i, v in enumerate(s_arr): # 제품목록 출력을 단축
        print(f"{i+1}.{v['prd_name']}:{v['price']:,}원")

    choice = int(input("원하는 번호를 입력하세요>>"))
    if choice == 1:
        no = int(input(f"{s_arr[choice-1]['prd_name']}를 구매하시겠습니까?(구매:1, 취소:0):"))
        if no == 1:
            print("구매완료")
            
            # 계산결과
            my_info['money'] -= s_arr[0]['price']
            # my_info['money'] = my_info['money'] - product[0]['price']
            print(f"m머니 : {my_info['money']}원")
        else:
            print("이전화면으로 이동합니다.")

        p_cal(choice)
    elif choice == 2:
        p_cal(choice) # 함수로 위의 출력을 단축
    elif choice == 3:
        p_cal(choice)
    elif choice == 4:
        p_cal(choice)
