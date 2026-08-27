import datetime

now = datetime.datetime.now()

print(now)
print(now.year)
print(now.month)

# format 함수 사용하여
# 123 -> 5자리 빈공백 0으로 채워서 출력하시오.

a = 123
print("{:05,d}".format(a)) # ,는 천단위로 ,표시해줌

print("{:015,d}".format(123456789))
print("{:02d}".format(8))

# 월을 출력할 때, 1~9월은 01~09월, 10월, 11월, 12월로 출력

import datetime

now1 = datetime.datetime.now()
month = now1.month

if month < 10:
    print("{:02d}월".format(month))
else:
    print("{:02d}월".format(month))

import datetime
now = datetime.datetime.now()
second = now.second
if second < 10:
    print("{:02d}초".format(second))
else:
    print("{:02d}초".format(second))

# 간략히 이렇게 출력도 가능
f_date = now.strftime("%Y년%m월%d일 %H시%M분%S초")
print(f_date)

