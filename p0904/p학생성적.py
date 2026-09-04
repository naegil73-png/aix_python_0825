# 학생성적관리 프로그램 : 입력, 출력, 수정, 삭제

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

# title = ["번호","이름","국어","영어","수학","합계","평균"]
# stu = []
# sno = 1

# def s_mainPrint(): # 메인화면 출력함수 선언
#     print("[학생성적프로그램]")
#     print("[1.학생성적입력]")
#     print("[2.학생성적출력]")
#     print("[3.학생성적수정]")
#     print("-"*60)
#     choice = int(input("원하는 번호를 입력하세요:"))
#     return choice

# def s_input(): # 학생성적 입력함수 선언
#     global sno
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
#         s_output() # 입력할 때마다 확인할 수 있음


# def s_output(): # 학생성적출력부분
#     print("[학생성적출력]")
#     print("-"*60)
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
#     print("-"*60)
#     if len(stu)==0:
#         print("*******학생데이터가 없습니다.********")
#     else:
#         for s in stu:
#             print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
#     print()


# # ---------------------------------------
# # 실제프로그램 시작부분 
# # ---------------------------------------
# while True:
#     choice = s_mainPrint() # 함수 호출

#     if choice == 1: # 학생성적입력부분
#         s_input()
#     elif choice == 2: # 학생성적출력부분
#         s_output()
#     elif choice == 3: # 학생성적수정 -> 검색기능이 있어야 함
#         print()
#         print("[학생성적수정]")
#         name = input("찾으려는 학생이름을 입력하세요.:")
#         temp = 0 # 찾았을 때만 출력하게 함
#         for i,s in enumerate(stu):
#             if s['name'] == name:
#                 print(f"{name}학생을 찾았습니다.")
#                 temp = 1
#                 break
#             # else: # 이 구문이 있으면 있는 학생도 찾을 때마다 없다는 문구가 나옴
#                 # print(f"{name}학생이 없습니다.")
#         if temp == 0: # 찾았을 때만 출력하게 함
#             print(f"{name}학생이 없습니다.")
#         elif temp == 1:
#             print('[과목수정선택]')
#             print("1.국어   2.영어  3.수학")
#             choice = int(input("원하는 번호입력:")) # 아래 수정하는 부분이 과목명을 제외하고 동일 -> 반복문으로 변경
#             if choice == 1: # 
#                 print(f"현재국어점수: {s['kor']}")
#                 s['kor'] = int(input("변경하려는 국어점수 :"))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3
#                 print(f"{s['kor']}점으로 국어점수가 변경되었습니다.")
#             elif choice == 2:
#                 print(f"현재영어점수: {s['eng']}")
#                 s['kor'] = int(input("변경하려는 영어점수 :"))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3
#                 print(f"{s['eng']}점으로 영어점수가 변경되었습니다.")
#             elif choice == 3:
#                 print(f"현재수학점수: {s['math']}")
#                 s['kor'] = int(input("변경하려는 수학점수 :"))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3
#                 print(f"{s['math']}점으로 수학점수가 변경되었습니다.")


#                 pass
#         print(i,s)



# title = ["번호","이름","국어","영어","수학","합계","평균"]
# k_title = ["no","name","kor","eng","math","total","avg"] # 추가
# stu = []
# sno = 1


# def s_mainPrint(): # 메인화면 출력함수 선언
#     print("[학생성적프로그램]")
#     print("[1.학생성적입력]")
#     print("[2.학생성적출력]")
#     print("[3.학생성적수정]")
#     print("-"*60)
#     choice = int(input("원하는 번호를 입력하세요:"))
#     return choice

# def s_input(): # 학생성적 입력함수 선언
#     global sno
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
#         s_output() # 입력할 때마다 확인할 수 있음


# def s_output(): # 학생성적출력부분
#     print("[학생성적출력]")
#     print("-"*60)
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
#     print("-"*60)
#     if len(stu)==0:
#         print("*******학생데이터가 없습니다.********")
#     else:
#         for s in stu:
#             print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
#     print()


# # ---------------------------------------
# # 실제프로그램 시작부분 
# # ---------------------------------------
# while True:
#     choice = s_mainPrint() # 함수 호출

#     if choice == 1: # 학생성적입력부분
#         s_input()
#     elif choice == 2: # 학생성적출력부분
#         s_output()
#     elif choice == 3: # 학생성적수정 -> 검색기능이 있어야 함
#         print()
#         print("[학생성적수정]")
#         name = input("찾으려는 학생이름을 입력하세요.:")
#         temp = 0 # 찾았을 때만 출력하게 함
#         for i,s in enumerate(stu):
#             if s['name'] == name:
#                 print(f"{name}학생을 찾았습니다.")
#                 temp = 1
#                 break
#             # else: # 이 구문이 있으면 있는 학생도 찾을 때마다 없다는 문구가 나옴
#                 # print(f"{name}학생이 없습니다.")
#         if temp == 0: # 찾았을 때만 출력하게 함
#             print(f"{name}학생이 없습니다.")
#         elif temp == 1:
#             print('[과목수정선택]')
#             print("1.국어   2.영어  3.수학")
#             choice = int(input("원하는 번호입력:")) 
#             print(f"현재{title[choice+1]}점수: {s[k_title[choice+1]]}")
#             s[k_title[choice+1]] = int(input("변경하려는 {title[choice+1] :"))
#             s['total'] = s['kor']+s['eng']+s['math']
#             s['avg'] = s['total']/3
#             print(f"{s[k_title[choice+1]]}점으로 국어점수가 변경되었습니다.")



#         print(i,s)


title = ["번호","이름","국어","영어","수학","합계","평균"]
k_title = ["no","name","kor","eng","math","total","avg"] # 추가
stu = []
sno = 1

# 파일 불러오기
# --------------------------------------------

f = open("C:/aaa/test2.txt","r",encoding="utf-8")
while True:
    line = f.readline() # /n 줄바꿈때문에 에러가 남.
    if line=="": break
    line = line.strip()

    print(line,end="")
    arr = line.split(",")

    for i,a in enumerate(arr):
        if 5>=i>=2:
            arr[i] = int(a)
        elif i==6:
            arr[i] = float(a)
    # stu 리스트에 저장
    # print(arr)
    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})


f.close()

# --------------------------------------------

def s_mainPrint(): # 메인화면 출력함수 선언
    print("[학생성적프로그램]")
    print("[1.학생성적입력]")
    print("[2.학생성적출력]")
    print("[3.학생성적수정]")
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
        s_output() # 입력할 때마다 확인할 수 있음


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
    elif choice == 3: # 학생성적수정 -> 검색기능이 있어야 함
        print()
        print("[학생성적수정]")
        name = input("찾으려는 학생이름을 입력하세요.:")
        temp = 0 # 찾았을 때만 출력하게 함
        for i,s in enumerate(stu):
            if s['name'] == name:
                print(f"{name}학생을 찾았습니다.")
                temp = 1
                break
            # else: # 이 구문이 있으면 있는 학생도 찾을 때마다 없다는 문구가 나옴
                # print(f"{name}학생이 없습니다.")
        if temp == 0: # 찾았을 때만 출력하게 함
            print(f"{name}학생이 없습니다.")
        elif temp == 1:
            print('[과목수정선택]')
            print("1.국어   2.영어  3.수학")
            choice = int(input("원하는 번호입력:")) 
            print(f"현재{title[choice+1]}점수: {s[k_title[choice+1]]}")
            s[k_title[choice+1]] = int(input("변경하려는 {title[choice+1] :"))
            s['total'] = s['kor']+s['eng']+s['math']
            s['avg'] = s['total']/3
            print(f"{s[k_title[choice+1]]}점으로 국어점수가 변경되었습니다.")



        print(i,s)


