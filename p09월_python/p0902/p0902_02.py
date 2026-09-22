# alist = [1,2,3]
# alist2 = []
# alist2 = alist # 얕은 복사
# alist3 = [*alist] # 깊은 복사, copy함수를 쓰기도 함

# print(alist)
# print(alist2)

# alist[0] = 100 # 리스트 값을 변경하면, alist2도 변경됨
# print(alist2)

# alist2[2] = 200
# print(alist)
# print(alist3) # 깊은 복사하면 값 변화없음

# a = 10
# a2 = 0
# a2 = a
# print(a2) # 변수는 값을 저장

# a = 100
# print(a2) # 값이 같은 다른 변수를 변경해도 해당 변수 값은 변경되지 않음. 리스트는 변경됨

# # 갯수를 반환하는 count함수
# aa = ["바나나","딸기","사과","딸기","딸기","사과"]
# print(aa.count("바나나"))
# print(aa.count("사과"))
# print(aa.count("딸기"))

# # 딕셔너리 : 자료의 추가, 삭제, 수정
# a_dic = {'바나나':1,'딸기':3,'사과':2}
# print(a_dic['바나나'])
# # 추가
# a_dic['배'] = 5
# print(a_dic)
# # 삭제
# del a_dic['바나나']
# print(a_dic)
# # 수정
# a_dic['사과'] = 100
# print(a_dic)

# # aa = ["바나나","딸기","사과","딸기","딸기","사과"] 를 딕셔너리 형태로 만듬

# aa = ["바나나","딸기","사과","딸기","딸기","사과"]
# aa_dic = {}
# for a in aa:
#     aa_dic[a] = 0
# print(aa_dic)
# # 여기까지는 딕셔너리 형태에 key값 반영, value는 미반영(위의 {} 형태 때문..)

# # 검색을 했을 때, 그 검색어의 검색결과를 알고 싶을 때 유용 -> 인기검색어
# aa = ["바나나","딸기","사과","딸기","딸기","사과"]
# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else:
#         aa_dic[a] += 1
# print(aa_dic)

# print(aa_dic.keys())
# print(list(aa_dic.keys())) # key값 반환 결과를 리스트로 변환

# # 다른 형태
# aa = [1,2,3,1,1,1,2,3,1,1,1,2,2,3]
# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else:
#         aa_dic[a] += 1
# print(aa_dic)

# # 리스트 만드는 방법
# a = [1,2,3,4,5] # 직접 입력
# a2 = [0]*10
# a3 = list(range(1,6))
# a4 = [i for i in range(1,6) if i%2 ==0 ] # 짝수만 입력하고자 할 때도 가능
# a4 = [i*i+2 for i in range(1,6) if i%2 ==0 ] # 짝수만 입력하고자 할 때도 가능. 이런 형태를 '리스트내포'라고 함
# print(a4)

# # 리스트 두개를 각 요소별로 묶을 때, zip함수
# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# # 이 두개를 c리스트에 넣고 싶으면
# c = []

# for i in range(len(a)):
#     c.append([a[i],b[i]])
# print(c)

# for i, j in zip(a, b): # for 문 두개, for i in a:와 for j in b:를 두개 실행하는 구문임
#     c.append([i,j])

# # 간단하게 이렇게 해결할 수 있음
# c = list(zip(a,b)) # 리스트 안의 튜플형태로 만들어줌(수정불가), 속도는 리스트보다 튜플이 빠름

# d = dict(zip(a,b)) # 딕셔너리로 묶어줌 
# print(d)

# # 프로그램에서 last in first out(대표적 : 뒤로가기), first in first out 2가지 방식이 있음. stack방식은 뒤로가기 방식

# aa = "가나다라가가나나다라라라라라라라"
# # 이를 딕셔너리로 변경하라

# aa_dic = {}
# for i in aa:
#     if i not in aa_dic:
#         aa_dic[i] = 1
#     else:
#         aa_dic[i] += 1
# print(aa_dic)

# aa = "a/b/c/d/f/g" # 각 요소를 분리
# aa_list = aa.split("/")
# print(aa_list)

# # 아래 bb열에 있는 모든 수의 합을 구하시오.
# bb = "100,10,5,4,1"
# # 순서 : 각 요소를 분리 -> 리스트화 -> 숫자로 변환 -> 합계 도출

# bb_list = bb.split(",") # 리스트로 변환함
# print(bb_list)

# bb_list2 = [int(i) for i in bb_list] # bb_list에 있는 각 요소를 숫자화하라.
# print(bb_list2)

# total = 0
# for i in bb_list2:
#     total += i
# print(total)

# # 문자열 찾기 : find, index(없으면 에러 -> 요소가 있는 지 확인 후 사용)

# ss = "파이썬 공부!! 열심히 합시다. 파이썬"
# print(ss.count("공부"))
# print(ss.count("파이썬")) # 갯수 반환
# print(ss.find("공부")) # 위치 값 반환
# print(ss.find("자바")) # 없을 때, -1 반환, rfind는 우측에서 찾음
# print(ss.startswith("파이썬"))
# print(ss.endswith("파이썬")) # 끝이 파이썬으로 끝나느냐 확인. 확장자 명 확인할 때 주로 사용

# # # 공백 제거 : strip
# # aa = input("이름을 입력하세요: ") # 이런 경우, space bar가 들어갈 경우, 찾아도 찾아지지 않는 경우가 많음
# # aa = input("이름을 입력하세요: ").strip() # 입력 시 입력문자 앞뒤 공백을 제거할 경우 사용

# # aa = [1,2,    3,4,5]
# # aa.strip()
# # print(aa)

# ss = "     파이썬" # 공백제거
# ss2 = "<<<<파<<이<썬" # < 제거

# ss1= ss.strip()
# print(ss1)

# ss3= ss2.replace("<","")
# print(ss3)

# # join 함수 : 추가요소.join(자료(또는 자료명)), 결합은 문자열만 가능(숫자는 불가)
# aa = "/"
# bb = aa.join("바나나")
# print(bb)

# aa = "/"
# bb = aa.join(["바나나","딸기","바나나"])
# print(bb)

# cc = "abc"
# aa = "/"
# bb = aa.join(cc)
# print(bb)

### 앞 뒤 공백제거 : strip()
a = "     abc     "
print(a.strip()) # 공백제거를 하나, 원 자료에 반영은 안됨
print(a) # 공백 그대로

### 중간공백 제거 : replace()
b = "    a     b    "
print(b.replace(" ",""))

c = "a,b,c,d,e" # 따옴표 안에 있는 것 모두 출력 - 문자열은 " "안에 있는 것 그대로 출력
print(c)
print(c.split(","))

### 분리 : split() -> 리스트 형태로 반환
a = "바나나, 딸기, 사과"
print(a.split(","))

# "1,홍길동,100,100,100,300,100" 이것을 국어 90점으로 변경하고, 합계와 평균을 구하고 다시 문자열로 변환
d = "1,홍길동,100,100,100,300,100"
dlist = d.split(",")
# 값을 수정하려면
dlist[2] = 90
dlist[3] = int(dlist[3])
dlist[4] = int(dlist[4])
dlist[5] = dlist[2]+dlist[3]+dlist[4]
dlist[6] = dlist[5]/3
dlist2 = [str(i) for i in dlist]
print(dlist)

# 문자열로 변경 - join함수
d_str = ",".join(dlist2)
print(d_str)

# count : 문자열 안에 해당문자가 몇개 있는 지 확인
# find : 문자열 안에 해당문자 위치 반환, 없으면 -1
# index : 문자열 안에 해당문자 위치 반환, 없으면 에러 발생
