# 로또맞추기
# 순서 : 랜덤번호 6개 생성
# 2.입력번호 6개 생성
# 3.랜덤번호, 입력번호 비교
# 4.결과 출력

import random
lotto = random.sample(range(1,46),6)
m_num = []
count = 0
c_num = []
i = 0
while i < 6:
    no = input("1~45사이 숫자선택:")
    if no.isdigit(): # 숫자 아닌 다른 문자를 입력했을 때 에러방지 목적..
        no = int(no)
        if no not in m_num:
                if no > 45 or no < 1:
                    print(no,"1~45사이 숫자를 고르세요")
                else:
                    m_num.append(no)
                    i += 1
        else:
            print(no,"이미 선택하셨습니다. 다른 번호를 선택하세요.")
for i in m_num:
    if i in lotto:
        count += 1
        c_num.append(i)
    else: print("숫자만 입력하세요.")

print("로또번호:",lotto)
print("선택번호:",m_num)
print("맞춘갯수:",count)
print("맞춘번호:",c_num)