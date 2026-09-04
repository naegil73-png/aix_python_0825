# title = ["번호","이름","국어","영어","수학","합계","평균"]
# stu = []

# sno = 1 # # 학생성적인원변수 -> 하나씩 카운트 되도록 번호부여 (DB에서 번호를 부여)

# while True:
#     print("[학생성적프로그램]")
#     print("[1.학생성적입력]")
#     print("[2.학생성적출력]")
#     print("-"*60)
#     choice = int(input("원하는 번호를 입력하세요:"))
#     print()

#     if choice == 1: # 학생성적입력
#         while True: # 입력을 멈추고 싶을 때까지 입력받음
#             no =sno
#             print("[학생성적입력]")
#             name = input(f"{no}번째 이름입력(0:이전화면이동): ")
#             if name == "0": break            
#             kor = int(input("국어점수입력: "))
#             eng = int(input("영어점수입력: "))
#             math = int(input("수학점수입력: ")) # 동일한 형태 -> for문으로 변경(score = 구문부터 for까지)
#             # score = [0]*3 # 원소가 3개인 리스트 생성 score = [0,0,0]
#             # for i in range(3):
#             #     score[i] = int(input(f"{title[i+2]}점수입력")) # 첫번째 입력 i = 0, 국어는 2번째 위치(i+2), 두번째는 i = 1, 영어는 1+2 = 3
#             total = kor+eng+math
#             avg = total/3

#             stu.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg})
#             print(f"{name}학생성적이 저장되었습니다.")

#             sno += 1

# # 순서 : 리스트저장 -> 파일저장 -> DB저장 -> web

# 함수로 변환 : 메인화면 출력, 

# title = ["번호","이름","국어","영어","수학","합계","평균"]
# stu = []
# sno = 1

# def s_mainPrint(): # 메인화면 출력함수 선언
#     print("[학생성적프로그램]")
#     print("[1.학생성적입력]")
#     print("[2.학생성적출력]")
#     print("-"*60)
#     choice = int(input("원하는 번호를 입력하세요:"))
#     return choice

# def s_input(sno): # 학생성적 입력함수 선언
#     while True: # 입력을 멈추고 싶을 때까지 입력받음
#         no = sno
#         print("[학생성적입력]")
#         name = input(f"{no}번째 이름입력(0:이전화면이동): ")
#         if name == "0": break            
#         kor = int(input("국어점수입력: "))
#         eng = int(input("영어점수입력: "))
#         math = int(input("수학점수입력: ")) # 동일한 형태 -> for문으로 변경(score = 구문부터 for까지)
#         # score = [0]*3 # 원소가 3개인 리스트 생성 score = [0,0,0]
#         # for i in range(3):
#         #     score[i] = int(input(f"{title[i+2]}점수입력")) # 첫번째 입력 i = 0, 국어는 2번째 위치(i+2), 두번째는 i = 1, 영어는 1+2 = 3
#         total = kor+eng+math
#         avg = total/3

#         stu.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg})
#         print(f"{name}학생성적이 저장되었습니다.")
#         print()
#         sno += 1
#     return sno

# while True:
#     choice = s_mainPrint() # 함수 호출

#     if choice == 1: # 학생성적입력
#         sno = s_input(sno)

# 다른 방법 : global 사용하면, 함수에 매개변수 없어도 됨

title = ["번호","이름","국어","영어","수학","합계","평균"]
stu = []
sno = 1

def s_mainPrint(): # 메인화면 출력함수 선언
    print("[학생성적프로그램]")
    print("[1.학생성적입력]")
    print("[2.학생성적출력]")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요:"))
    return choice

def s_input(): # 학생성적 입력함수 선언
    global sno
    while True: # 입력을 멈추고 싶을 때까지 입력받음
        no = sno
        print("[학생성적입력]")
        name = input(f"{no}번째 이름입력(0:이전화면이동): ")
        if name == "0": break            
        kor = int(input("국어점수입력: "))
        eng = int(input("영어점수입력: "))
        math = int(input("수학점수입력: ")) # 동일한 형태 -> for문으로 변경(score = 구문부터 for까지)
        # score = [0]*3 # 원소가 3개인 리스트 생성 score = [0,0,0]
        # for i in range(3):
        #     score[i] = int(input(f"{title[i+2]}점수입력")) # 첫번째 입력 i = 0, 국어는 2번째 위치(i+2), 두번째는 i = 1, 영어는 1+2 = 3
        total = kor+eng+math
        avg = total/3

        stu.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg})
        print(f"{name}학생성적이 저장되었습니다.")
        print()
        sno += 1
    return sno

def s_output(): # 학생성적출력부분
    print("[학생성적출력]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    if len(stu)==0:
        print("*******학생데이터가 없습니다.********")
    else:
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
    print()


# ---------------------------------------
# 실제프로그램 시작부분 
# ---------------------------------------
while True:
    choice = s_mainPrint() # 함수 호출

    if choice == 1: # 학생성적입력부분
        s_input()
    elif choice == 2: # 학생성적출력부분
        s_output()