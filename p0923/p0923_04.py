from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# 2. selenium : 자동화 구현
# 상단 제어창문구 삭제
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options) # 셀레니움을 통해 설정된 옵션값이 크롬 브라우저에 적용되도록 함
# browser.maximize_window() # 화면 최대창 확대
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B2%BD%EC%A3%BC&autoKeyword=%EA%B2%BD%EB%B6%81+%EA%B2%BD%EC%A3%BC%EC%8B%9C&checkIn=2026-09-23&checkOut=2026-09-24&personal=2"
# browser.get(url)
# time.sleep(2)

# 먼저 실행해서 마지막 장소까지 페이지에 나타나게 해서 파일 저장하고 참조 설정
# # 자바스크립트를 통해 브라우저 높이 가져오기
# pre_height = browser.execute_script('return document.body.scrollHeight') # document.body.scrollHeight은 현재 웹페이지의 세로높이 값을 파이썬에 반환하라. 그것을 크롬 콘솔창에 적용하라
# print("처음 높이 : ",pre_height)
# while True:
#     # 스크롤 내리기
#     browser.execute_script('window.scroll(0,document.body.scrollHeight)') # 크롬 콘솔창에 입력된 값에 현재창의 맨 밑바닥 값을 적용하라
#     time.sleep(3) # 내용추가하는데 시간대기

#     # 다시 높이 가져오기
#     next_height = browser.execute_script('return document.body.scrollHeight') # 
#     print('변경된 높이 : ',next_height)

#     if pre_height==next_height: break
#     else : pre_height = next_height

# print('더 이상 높이 변경이 없음')

# 높이 조정 이후 파일 저장 및 읽기
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('yeogi1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 파일 저장해서 저장한 파일을 가지고 정보를 가져오기
# 이미지, 숙소명, 별점
with open('yeogi1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

s_ul = soup.find("ul",{"class":"css-y5z6rw"})
lis = s_ul.find_all("li")
print(len(lis))
for idx,li in enumerate(lis):
    print(f"{idx+1}")
    try:
        s_img = li.find('img')['src'] 
        print("이미지 : ",s_img)
        s_title = li.find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1gsfgy5'}).get_text(strip=True)
        print("숙소명 : ",s_title)
        s_star = li.find('span',{'class':'css-ry30z7'}).get_text(strip=True)
        s_star = float(s_star)
        print("평점 : ",s_star)
        s_view = li.find('span',{'class':'css-144z61f'}).get_text(strip=True)
        s_view = int(s_view[:-4].replace(',',''))
        print("평가수 : ",s_view)
        s_price = li.find('span',{'class':'css-1llao6q'}).get_text(strip=True)
        s_price = int(s_price.replace(',',''))
        print("금액 : ",s_price)
        print("-"*60)
        
    except Exception as e:
            pass