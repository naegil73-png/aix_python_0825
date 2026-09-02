import random
def ran_number(choice):
    if choice == 1:
        # 랜덤숫자 5개
        result = random.sample(range(1,101),5)
    elif choice == 2:
        # 랜덤숫자 3개
        result = random.sample(range(1,101),3)
    else:
        # 랜덤숫자 1개
        result = random.sample(range(1,101),1)
    return result

while True:
    # 랜덤숫자는 1~100사이 -> 아래의 print문 3개는 없어도 됨
    print("1. 랜덤숫자 5개 가져오기")
    print("2. 랜덤숫자 3개 가져오기")
    print("3. 랜덤숫자 1개 가져오기")
    choice = int(input("원하는 번호를 입력하세요. >>"))
    result = ran_number(choice)
    print("결과:",result)
    

    def main_print():
            # 랜덤숫자는 1~100사이 
        print("1. 랜덤숫자 5개 가져오기")
        print("2. 랜덤숫자 3개 가져오기")
        print("3. 랜덤숫자 1개 가져오기")
        choice = int(input("원하는 번호를 입력하세요. >>"))
        return choice