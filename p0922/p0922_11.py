# 사이트 자동화 프레임워크 : selenium -> 
# pip install selenium 설치
# https://storage.googleapis.com/chrome-for-testing-public/153.0.8010.52/win64/chromedriver-win64.zip 에서 다운 받음 -> exe파일을 작업경로에 넣음


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# # 2.selenium 파일저장
# browser = webdriver.Chrome()
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('stock1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# selenium 실행과정
# 1.브라우저 실행 및 설정(크롬 드라이브 열기) : 
# browser = webdriver.Chrome()
# 2. 원하는 url 페이지 로딩: 
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# browser.get(url)
# 3. 데이터 로딩 대기
# time.sleep(3)
# 4. 데이터 추출방법(2가지 방식)
# 1방식 : soup = BeautifulSoup(browser.page_source, "lxml")
#       with open("stock1.html", "w", encoding="utf-8") as f:
#       f.write(soup.prettify())
#       trs = soup.select("tbody tr")

# 2방식 : elements = browser.find_elements(By.CSS_SELECTOR, "tbody tr") # 이 방식 사용
            # 조건을 만족하는 태그 여러개를 찾아라(태그를 검색기준으로 옆에 제시된 검색어에 의해 찾겠다.)
        # for el in elements:
        # print(el.text)

# 5. browser.quit()


# # 파일 BeautifulSoup변환
# with open('stock1.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')

# s_tbody = soup.find("tbody",{'class':'Table_tbody__EJrOg'})
# trs = s_tbody.find_all('tr')
# tds = trs[0].find_all('td')
# print(tds[0].find('span',{'class':'SingleLineText_text__HI_cb'}).get_text(strip=True))


# print("완료")

# 1.requests 방식으로 파일저장
# url = "https://www.melon.com/chart/index.htm"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료

# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
# with open('melon1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())