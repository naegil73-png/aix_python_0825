# 딕셔너리 : key와 value로 구성, key는 숫자, 문자가 올 수 있으나, 대체로 문자를 씀. value는 문자, 숫자가 반반으로 사용됨

stu = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"music":100} # 리스트와 달리, 어떤 항목의 값인지 대략 파악가능함. 딕셔너리를 많이 씀

stu["total"] = (stu["kor"]+stu["eng"]+stu["math"]+stu["music"]) # stu에 없는 total을 이렇게 하면, stu에 추가가 됨
print(stu)

stu["avg"] = stu["total"]/4
print(stu)

# 딕셔너리 수정 : 있는 키 값에 값을 넣으면 수정됨
stu["kor"] = 50
print(stu)
print(stu["kor"]) # key로 출력하면, value가 출력됨

# 딕셔너리 삭제 : del(키)
del(stu["eng"])
print(stu)

# 공공데이터 형태 : [ { }, { }, ...] 리스트 내의 딕셔너리 형태의 자료

stu_list = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":400,"avg":100},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":400,"avg":100},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":400,"avg":100}
]

stu_list[0]["name"] = "홍길자"
print(stu_list[0]['name'])
print(stu_list[0]['kor'])
# stu_list['rank'] = 1
print(stu_list)

# student['주소']
# student.get['주소'] -> 위와 동일한 결과이나, 해당 자료가 없어도 에러가 나지 않음. 위의 구문은 에러남

# print(stu_list.keys()) # 결과는 dict-keys..로 결과가 나옴
# print(stu_list.values()) # 결과는 리스트로 나오지 않음
# print(stu_list.items) # key, value 모두 나오는 구문임

# s_list = list(stu_list.values()) # 이렇게 리스트로 변환해서 사용해야 함

# 딕셔너리 추가
singer = {}

singer["이름"] = "트와이스"
singer["멤버"] = 9

print(singer)

stu = {"no":1, "name":"홍길동", "total":100}

# 딕셔너리 정렬 
# 가급적 정렬, 삭제는 하지 말 것. 정렬, 삭제는 DB에서 하는 것이 좋음

# name_dic = {
#     "aaa":"토마토", "bbb":"바나나", "eee":"딸기", "bbb":"배"
# }
# name_sort1 = sorted(name_dic.items(),key=operator.itemgetter(0))

engs = {
    "car":"자동차",
    "color":"색상",
    "pig":"돼지",
    "love":"사랑",
    "phone":"전화기"
}

while True:
    for k, v in engs.items():
        print(k,"는(은) 한국어로 무엇일까요?")
        answer = input("정답:")
        if answer == v:
            print("정답")
            break
        else:
            print("오답")
    break
# 집합 : 순서와 중복이 없는 자료형

myset = {1,2,3,4,5}

alist = [i for i in range(1,10)]
print(alist)

# 

name_dic = {
    "aaa":"토마토", "bbb":"바나나", "eee":"딸기", "bbb":"배"
}
import operator
name_sort1 = []
name_sort1 = sorted(name_dic.items(),key=lambda x:x[1]) # 1로 하면 value로 정렬, 0을 입력하면 key로 정렬, 역순 정렬하려면, 맨 끝에 reverse = True 추가
name_sort1 = sorted(name_dic.items(),key=lambda x:x[1], reverse=True)
print(name_dic)

# 
alist = list(range(1,21))
nlist = [] # 3의 배수만 넣겠다면..
for i in alist:
    if i%3 == 0:
        nlist.append(i)
print(nlist)

# 위의 구문은 아래로 간략히 단축할 수 있음
a = [n for n in range(1,21) if n%3 ==0]
print(a)