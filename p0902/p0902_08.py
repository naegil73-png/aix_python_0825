from func import* # 다른 파일에 있는 함수를 불러와서 실행문만 작성, 실행하면 결과 도출됨

# 프로그램 시작 ------------------------------------------------

while True:
    choice = main_print()
    result = ran_number(choice)
    print("결과 :", choice)

# 함수 사용이유:
# 1. 중복코드 재사용
# 2. 간결하게 사용 가능