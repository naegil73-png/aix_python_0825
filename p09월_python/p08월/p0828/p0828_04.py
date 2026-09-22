# 문자열 함수
# split, strip, replace, find, rfind


paper = '''\
네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
이번 홍수의 원인으로 지목된 것처럼 
산 위의 빙하가 붕괴되면서 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다.\
'''

print(paper)
print(len(paper)) # 길이를 알려고 할 때 사용. 매우 자주 사용, 중요

str1 = "1,홍길동,100,100,100,300,100" # 문자열타입
s = str1.split(",") # ******** split: 특정문자를 기준으로 각 요소를 분리해 줌. 아주 중요, 자주 사용
print(s)
print(s[2])


str2 = "2026-08-28"
s2 = str2.split("-")
print(s2)
print(s2[2])

str3 = "안녕 반가워 다음에 봐"
s3 = str3.split(" ")
print(s3)
print(s3[1])

# 공공데이터 포털 : 네이버 naegil2 사용.
# 공공데이터 포털의 파일은 리스트, 딕셔너리로 구성. 갯수 파악은 리스트 형태가 좋음. 값에 대한 파악은 딕셔너리 형태가 좋음
# 공공데이터 파일 데이터는 CSV(쉼표로 구분 -> split(","))
# 위치 찾기 : 위도, 경도 등이 CSV로 저장되어 있음

str4 = "EDMS,307-2E-PS-W-611-W008,VF5770" # 공공데이터포털의 CSV파일 중 하나
s4 = str4.split(",") # split을 쓰면, 문자열을 리스트로 반환
print(s4)
print(s4[2])

# strip - 공백제거
aaa1 = "                안녕하세요.                            "
print(aaa1)
print(aaa1.strip())

aaa2 = "    안녕    하세요.    " # 요소 사이에 있는 공백은 제거 불가
print(aaa2.strip())

# replace : 문자를 다른 문자로 대체
print(aaa2.replace(" ","")) # 글자 사이를 붙이려면, replace("before", "after")

aaa3 = "aabbccddaaeea"
aaa4 = aaa3.replace("a","k")
print(aaa4)

# find : 검색함수, 왼쪽부터 검색시작, 있으면 위치를 반환, 없으면 -1을 반환
bb = "abcdefghicba"
print("i" in bb)
print(bb.find("f"))
print(bb.find("k"))

# 오른쪽에서 검색하게 하려면
print(bb.rfind("c")) # c가 2개인데, 9번째 있는 c를 찾아줌