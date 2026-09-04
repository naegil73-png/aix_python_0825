# 예외처리

# 오류 발생 
# print(1) -> pront(1)로 입력 : 구문오류(실행자체가 안됨)

# arr = [1,2,3,4,5]
# while True:
#     choice = int(input("0~4까지 숫자입력:"))
#     print("선택값 :",arr[choice]) # choice에 0~4까지만 출력됨. 5를 입력하면, 오류 -> 런타임에러(실행은 되나, 오류 발생)
# # 에러가 나면, 새로 실행해야 하기 때문에 기존의 처리내용이 다 날아감
#     break

# # 에러가 났을 때, 처리해 주는 것
# arr = [1,2,3,4,5]
# while True:
#     choice = int(input("0~4까지 숫자입력:"))
#     if choice > 4:
#         print('값을 잘못 입력하셨습니다.')
#     print("선택값 :",arr[choice])

#     break

# # 에러가 날만한 곳에 try구문을 입력해 줌.
# '''
# try:
#     에러가 발생할만한 코드
# except:
#     에러 발생 시 처리코드

# '''

# arr = [1,2,3,4,5]

# while True:
#     try:
#         choice = int(input("0~4까지 숫자입력:"))
#         if choice > 4:
#             print('값을 잘못 입력하셨습니다.')
#         print("선택값 :",arr[choice])
#     except:
#         print("에러가 났습니다.")

    
# arr = [1,2,3,4,5]

# while True:
#     choice = int(input("0~4까지 숫자입력:"))
#     print("선택값 :",arr[choice])
#     # try:
#     #     choice = int(input("0~4까지 숫자입력:"))
#     #     if choice > 4:
#     #         print('값을 잘못 입력하셨습니다.')
#     #     print("선택값 :",arr[choice])
#     # except Exception as e: # Exception as e는 e를 출력하면(누르면?) 에러의 원인을 표시해줌
#     #     print("에러가 났습니다.")
#     #     print(e)

# 가급적 try, except 사용하지 말 것(java, C에서는) : 사용은 연결된 장비, DB의 전원 등이 나갔을 때.. 그 외에는..
# web에서 Data 가져올 때, 자료에 오류가 있는 경우, 예외처리는 가능할 듯

# # 에러가 안나는 프로그램으로 만들어야 함
# while True:
#     choice = input("숫자입력:")
#     if choice.isdigit():
#         choice1 = int(choice)
#         break
#     else:
#         print("숫자를 입력해주세요")
#         continue

print(1)
try:
    print(2)
    print(3)
    print(10/0) # 에러가 남
    print(4)
except:
    print(5)
    print(6)
print(7)
# 위 구문의 결과는 1,2,3,5,6,7 (1,2,3,에러 발생-> except구문 5,6,7)
# print(10/0)이 없으면.. 1,2,3,4 except구문은 실행안됨(에러 발생 안되었기 때문)

print(1)
try:
    print(2)
    print(3)
    print(10/0) # 에러가 남
    print(4)
except Exception as e: # 이 구문은 알아둘 것
    print(e)
    print(Exception)
    print(5)
    print(6)
print(7)

# indexerror : 범위, valueerror: 문자, 숫자 오류

# try, except(에러발생시 처리방법), else(에러발생치 않았을 때 처리방법)

# try, except(에러발생시 처리방법), else(에러발생치 않았을 때 처리방법), Finally(에러가 나든, 안나든 무조건 실행) # finally는 자주 씀

# 에러를 표시할 때, Exception, Exception Valuerror... 등이 나오면.. Exception을 맨 밑에 써야 다른 것도 실행됨



# raise : 강제로 에러를 발생시키는 것

# print(1)
# print(2)
# print(3)
# raise NotImplementedError 
# print(4)
# print(5)
# print(6)
# print(7)


choice = int(input("원하는 번호입력:"))
if choice == 1:
    print("학생성적입력부분")
if choice == 2:
    print("학생성적출력부분")
if choice == 3:
    print("학생성적수정부분")
if choice == 4: # 4번 구문은 구현하지 않았을 경우, 확인하기 위해 발생시키는 에러
    raise NotImplementedError

# 오류, 예외에도 상속관계가 있음

