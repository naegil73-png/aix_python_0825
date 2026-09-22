s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2

my_info = {"id":"aaa","pw":1111,"money":10000000,"point":0}

for i, v in enumerate(s_arr):
    print(f"{i+1}.{v['prd_name']}") # for i, v in enmerate(s_arr):print(f"{i+1}.{v['prd_name']}) 
    # 딕셔너리에서 enumerate는 하나의 요소{}를 인덱스와 하나의 요소{}로 만들어줌 -> 0:{"prd_name":"컴퓨터","price":1000000}, 1:... 이런 형태

print("-"*60)

def cal():
    if my_info['money'] < s_arr[choice-1]['price']:
        print("잔액이 부족합니다.")

while True:
    print("1.컴퓨터")
    print("2.냉장고")
    print("3.오디오")
    print("4.세탁기")
    choice = int(input("원하는 번호입력 : "))
    if choice == 1:
        print("컴퓨터")
        num = int((input('구매결정(1:구매, 0:취소):')))
        if num == 1:
            send = s_arr[choice-1]['price']
            print(f'컴퓨터 대금 {[send]}가 지출되었습니다.')
            my_info['money'] -= s_arr[choice-1]['price']
            print(f"잔고는 {[my_info['money']]}원 입니다.")
            cal()
            
    elif choice == 2:
        print("냉장고")
        num = int((input('구매결정(1:구매, 0:취소):')))
        if num == 1:
            send = s_arr[choice-1]['price']
            print(f'냉장고 대금 {[send]}가 지출되었습니다.')
            my_info['money'] -= s_arr[choice-1]['price']
            print(f"잔고는 {[my_info['money']]}원 입니다.")
            cal()

    elif choice == 3:
        print("오디오")
        num = int((input('구매결정(1:구매, 0:취소):')))
        if num == 1:
            send = s_arr[choice-1]['price']
            print(f'오디오 대금 {[send]}가 지출되었습니다.')
            my_info['money'] -= s_arr[choice-1]['price']
            print(f"잔고는 {[my_info['money']]}원 입니다.")
            cal()

    elif choice == 4:
        print("세탁기")
        num = int((input('구매결정(1:구매, 0:취소):')))
        if num == 1:
            send = s_arr[choice-1]['price']
            print(f'세탁기 대금 {[send]}가 지출되었습니다.')
            my_info['money'] -= s_arr[choice-1]['price']
            print(f"잔고는 {[my_info['money']]}원 입니다.")
            cal()
