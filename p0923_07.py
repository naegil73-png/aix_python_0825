from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# for i in range(2016,2023):
#     m_url = f'https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
#     print(m_url)

#     options = Options()
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     browser = webdriver.Chrome(options=options)
#     browser.maximize_window()

#     url = m_url
#     browser.get(url)
#     time.sleep(3)

#     soup = BeautifulSoup(browser.page_source, 'lxml') # bs로 변환하는 것은 아래의 prettify를 하기 위한 것
#     with open(f'p0923/file/movie_{i}.html','w',encoding='utf-8') as f:
#         f.write(soup.prettify())
#         time.sleep(2)

# 파일 BeautifulSoup변환
for i in range(2016,2023):
    print(f'p0923/file/movie_{i}.html')
    with open(f'p0923/file/movie_{i}.html','r',encoding='utf-8') as f:
        soup = BeautifulSoup(f,'lxml') # 읽은 소스를 bs로 변환, 가공 준비

    with open('p0923/file/movie_2022.html','r',encoding='utf-8') as f:
        soup = BeautifulSoup(f,'lxml')

# ******* 소스코드를 보고 위치 결정(중요) -> 여러개 찾을 경우, 전체를 아우르는 박스, tbody, div, a, class 등. class, id(유일한 주소)가 있으면 좋음

#     # m_ul = soup.find('ul',{'class':'c-list-basic ty_flow35'})
#     # lis = m_ul.find_all('li')
#     # print(f'[ {idx}년 영화 ]')
#     # for i in range(5):
#     #     # 1. 이미지링크
#     #     m_img = lis[i].find('img')['src']
#     #     print(m_img)
#     #     # 2. 영화제목
#     #     m_title = lis[i].find('strong',{'class':'tit-g clamp-g'}).get_text(strip=True)
#     #     print(m_title)
#     #     # 3. 누적관객수
#     #     m_desc = lis[i].find('p',{'class':'conts-desc clamp-g'}).get_text(strip=True)
#     #     print(int(m_desc[3:-2].replace(",","")))
#     #     # 4. 개봉날짜
#     #     m_date = lis[i].find('span',{'class':'conts-subdesc clamp-g'}).get_text(strip=True)
#     #     print(m_date)
#     #     print('-'*50)