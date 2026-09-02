import random
import datetime # 현재시간을 가져오는 클래스 선언

# 현재시간
now  = datetime.datetime.now()
print("전체:",now) # 컴퓨터에 나오는 시간을 가져옴
print("년도:",now.year) # 년도만
print("월:",now.month) # 월만
print("일:",now.day) # 일만
print("시:",now.hour) # 시
print("분:",now.minute) # 분
print("초:",now.second) # 초

# from datetime import datetime으로도 가능

# 위의 결과를 2026년 8월 27일 11시 12분 10초로 나타내시오.
import datetime
now = datetime.datetime.now()
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

# slak 대화방의 내용을 vscode에 붙여넣으면 에러가 발생 -> 메모장에 붙였다가 다시 vscode에 붙여넣어야 함

# if문을 써서 1~6월까지는 상반기
# 7~12월까지는 하반기
# 현재월을 datatime함수를 사용해서 검색한 다음
# 상반기, 하반기 인지 출력하시오.
# 순서 : 날짜함수를 사용해서 월을 변수에 저장한 후 비교, 출력

import datetime

now = datetime.datetime.now()
month = now.month

if month >= 7:
    print("지금은 {}월, 하반기입니다.".format(month))
else:
    print("지금은 {}월, 상반기입니다.".format(month))

