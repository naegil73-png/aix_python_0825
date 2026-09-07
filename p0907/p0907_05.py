s_title = ["no","name","kor","eng","math","total","avg","rank"]
stu = ["1","홍길동",100,100,100,300,100.0,0] 
# 위의 두가지 리스트를 한꺼번에 묶어서 딕셔너리로 변환

s_dic = dict(zip(s_title,stu))
print(s_dic)