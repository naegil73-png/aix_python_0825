# def str_print(n,*v): # 매개변수는 2개가 있음. 하지만, *가 있기 때문에 가변매개변수
#     pass

# str_print((3,"안녕","반가워","잘있어")) # 함수호출에서 4개의 매개변수가 있음 -> 함수 선언에서도 변수가 4개여야 함. 하지만, 가변매개변수로 되어 있으면, 가능


# def str_print(n,*v):
#     for i in range(n):
#         for j in v:
#             print(j,end="")
#         print()

# str_print(3,"안녕","반가워","잘있어") # 여기서 3 = n, "안녕","반가워","잘있어" = *v구문에 입력


# print(1,2,3,4,5) # 함수 안에 있기 때문에 요소는 무한정으로 받을 수 있음
# print(1,2,3,4,5, sep = "--") # 요소 간의 구분자를 --로 설정
# print("번호","이름","국어","영어",sep="\t")

# # 이렇게로도 표현 가능
# arr = ["번호","이름","국어","영어"]
# print(*arr,sep="\t") # *arr은 전개연산자

# # # 이렇게 하면 에러가 남
# # def str_print(*v,n):
# #     print(n)

# # 변수의 종류 : 일반매개변수, 초기화매개변수, 가변매개변수, 키워드매개변수

# str_print(1,2,3,4,5,"안녕") # 여기서 1~5, 안녕까지 모두 *v로 들어감 -> n은 값이 안들어감 => 따라서 일반매개변수를 앞, 가변매개변수를 뒤에 써야 함

# # 이렇게 해야 함
# def str_print(n,*v):
#     print(n)

# str_print(1,2,3,4,5,"안녕") # 여기서 1만 n, 2~5, 안녕까지 모두 *v로 들어감

# # 가변매개변수를 앞에 쓰고 싶으면..
# def str_print(*v,n):
#     print(n)

# str_print(1,2,3,4,5,n="안녕") # 가변매개변수가 앞에 왔을 경우에는 키워드매개변수를 사용해야 함. 키워드매개변수는 마지막에 있어야 함

# 아래의 두 변수는 잘 쓰지 않음
# 가변매개변수 - 맨 뒤쪽에 배치
# 키워드매개변수 - 맨 뒤쪽에 배치 * 만약, 가변매개변수와 같이 사용하게 될 경우에도 키워드매개변수가 맨 뒤쪽에 배치

# # return은 함수의 종료, 끝남. return을 만나면, 함수의 값을 반환한다.

# def sum_all(start=0, end = 100, step=1):
#     output = 0

#     for i in range(start, end+1, step):
#         output += i
#     return output

# sum_all(10) # 10을 넣으면, start에 10이 입력되고, 입력되지 않은 end, step은 각각 100, 1을 넣어서 실행됨

# # 함수에서 3개 매개변수를 써야하나, 1개만 입력하면 에러가 남.
# def cal(s1,e1,s2):
#     print(s1,e1,s2)

# # cal(0) # 

# def cal(s1=1,e1=50,s2=10):
#     print(s1,e1,s2)

# cal() # 아무것도 입력치 않으면, 초기 값을 적용해서 1, 50, 10을 넣음
# cal(5) # start에 5넣음
# cal(end=100) # 다른 것은 그대로 하고, end = 100으로 입력해라

# 변수 선언부분
# 개인정보
my_info = {"id":"aaa","pw":"1111",\
           "money":10_000_000,\
            "bonusPoint":0}
# 구매리스트
cart = []

product = [
    {"p_name":"컴퓨터", "price":1000000, "bonusPoint":1000000*0.1},
    {"p_name":"세탁기", "price":2000000, "bonusPoint":2000000*0.1},
    {"p_name":"오디오", "price":500000, "bonusPoint":500000*0.1}
]

while True:
    print("쇼핑몰에 오신 것을 환영합니다.")
    id = input("아이디: ")
    pw = input("패스워드: ")

    if my_info["id"] == id and my_info["pw"] == pw:
        print("로그인이 되었습니다.")
        break
    else:
        print("아이디나 패스워드를 확인해 주세요.")

# my금액, 보너스 포인트
print(f"현재 보유금액 : {my_info['money']:,}원")
print(f"현재 보너스포인트 : {my_info['bonusPoint']:,}포인트")
print("-"*40)

while True:
    print()
    print("[쇼핑몰 구매사이트]]")
    for i, p in enumerate(product):
        print(f"{i+1}. {p['p_name']} : {p['price']:7,}원")
    print("9. 구매상품리스트")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요:"))
    print()

    if choice == 1:
        no = int(input("컴퓨터를 구매하시겠습니까?(구매:1, 취소:0):"))
        if no == 1:
            print("구매완료")
            
            # 계산결과
            my_info['money'] -= product[0]['price']
            my_info['bonusPoint'] += product[0]['bonusPoint']
            # my_info['money'] = my_info['money'] - product[0]['price']
            print(f"m머니 : {my_info['money']}원")
            print(f"m보너스포인트 : {my_info['bonusPoint']}포인트")
        else:
            print("이전화면으로 이동합니다.")
    
    elif choice == 2:
        no = int(input("세탁기 구매하시겠습니까?(구매:1, 취소:0):"))
        if no == 1:
            print("구매완료")
            my_info['money'] -= product[1]['price']
            my_info['bonusPoint'] += product[1]['bonusPoint']
            print(f"m머니 : {my_info['money']}원")
            print(f"m보너스포인트 : {my_info['bonusPoint']}","원")
            
        else:
            print("이전화면으로 이동합니다.")
    
    if choice == 3:
        no = int(input("오디오를 구매하시겠습니까?(구매:1, 취소:0):"))
        if no == 1:
            print("구매완료")
            my_info['money'] -= product[2]['price']
            my_info['bonusPoint'] += product[2]['bonusPoint']
            print(f"m머니 :", my_info['money'])
            print(f"m보너스포인트 : {my_info['bonusPoint']}")           
        else:
            print("이전화면으로 이동합니다.")
        break


# 함수로 작성

# 변수 선언부분
# 개인정보
my_info = {"id":"aaa","pw":"1111",\
           "money":10_000_000,"bonusPoint":0}
# 구매리스트
cart = []
# 상품
product = [
    {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
    {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
    {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1},
]

def cal1(choice):
    no = int(input(f"{product[choice-1]['p_name'] }를 구매하시겠습니까?(구매:1,취소:0) "))
    if no == 1:
        print(f"{product[choice-1]['p_name'] } 구매완료")
        # 계산후 결과
        my_info['money'] -= product[choice-1]['price']
        # my_info['money'] = my_info['money'] - product[0]['price']

        my_info['bonusPoint'] += product[choice-1]['bonusPoint']
        print(f"m머니 : {my_info['money']:,}원")
        print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")
    else:
        print("이전화면으로 이동합니다.")



# 아이디,패스워드 확인
while True:
    print("[ 쇼핑몰에 오신것을 환영합니다. ]")
    id = input("아이디 : ")
    pw = input("패스워드 : ")

    if my_info["id"] == id and my_info["pw"]==pw:
        print("로그인이 되었습니다.")
        break
    else:
        print("아이디 또는 패스워드가 일치하지 않습니다.")

# my금액,보너스포인트
print(f"현재 보유금액 : {my_info['money']:,}원")
print(f"현재 보너스포인트 : {my_info['bonusPoint']:,}포인트")
print("-"*40)
# 구매정보
while True:
    print()
    # 상품출력부분
    print("[ 쇼핑몰 구매사이트 ]")
    for i,p in enumerate(product):
        print(f"{i+1}. {p['p_name']} : {p['price']:,}원")
    print("9. 구매상품리스트")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()


    # 1.컴퓨터구매부분
    if choice == 1:
        cal1(choice)
    elif choice == 2:
        cal1(choice)
    elif choice == 3:
        cal1(choice)