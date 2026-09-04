# 예외처리

# 오류 발생 
# print(1) -> pront(1)로 입력 : 구문오류

# arr = [1,2,3,4,5]
# while True:
#     choice = int(input("0~4까지 숫자입력:"))
#     print("선택값 :",arr[choice]) # choice에 0~4까지만 출력됨. 5를 입력하면, 오류 -> 런타임에러
# # 에러가 나면, 새로 실행해야 하기 때문에 기존의 처리내용이 다 날아감
#     break

# 에러가 났을 때, 처리해 주는 것
arr = [1,2,3,4,5]
while True:
    choice = int(input("0~4까지 숫자입력:"))
    if choice > 4:
        print('값을 잘못 입력하셨습니다.')
    print("선택값 :",arr[choice])

    break

# 에러가 날만한 곳에 try구문을 입력해 줌.
'''
try:
    에러가 발생할만한 코드
except:
    에러 발생 시 처리코드

'''

arr = [1,2,3,4,5]

while True:
    try:
        choice = int(input("0~4까지 숫자입력:"))
        if choice > 4:
            print('값을 잘못 입력하셨습니다.')
        print("선택값 :",arr[choice])
    except:
        print("에러가 났습니다.")