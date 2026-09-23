from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# 2. selenium : 자동화 도구
# browser = webdriver.Chrome() 
# # browser는 어떤 브라우저를 어떻게 제어할 것인가를 할당받는 것
# # webdriver는 파이썬이 크롬브라우저를 직접 제어할 수 있도록 해주는 중계자 역할(열리고, 닫고, 저장, 입력 등) -> ~Chrome은 webdriver로 크롬을 제어하겠다
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# # 브라우저 열기
# browser.get(url)
# time.sleep(4)
# 파일저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('stock1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 파일 BeautifulSoup변환
with open('stock1.html','r',encoding='utf-8') as f: # 위에서 파일을 만든 후, 참조처리함
    soup = BeautifulSoup(f,'lxml')

#------------------------------------한개씩
# s_tbody = soup.tbody
# trs = s_tbody.find('tr')      # 1개 sk하이닉스 find,find_all

# tds = trs.find_all('td')      # td 8개
# s_title = tds[0].find('span',{'class':'SingleLineText_text__HI_cb'})
# s_title = s_title.get_text(strip=True)
# s_index = tds[0].find("span",{"class":"index"})
# s_index = s_index.get_text(strip=True)
# s_price = tds[1].find("span",{"class":"SingleLinePrice_price__g_6VV"})
# s_price = s_price.get_text(strip=True)
# s_amount = tds[7].find("span",{"class":"SingleLineText_text__HI_cb"})
# s_amount = s_amount.get_text(strip=True)
# tds[7]
# # trs = s_tbody.find_all('tr')  # 100개 정보
# print(f"{s_index},{s_title},{s_price},{s_amount}")

# 순환문
s_tbody = soup.tbody
trs = s_tbody.find('tr')      # 1개 sk하이닉스 find,find_all

s_headTitle = []
s_tr = soup.thead.tr
ths = s_tr.find_all('th') # 8개 정보
for th in ths:
    s_headTitle.append(th.get_text(strip=True))
print(s_headTitle)
trs = s_tbody.find_all("tr")
for tr in trs:
    tds = tr.find_all('td')      # td 8개
    s_index = tds[0].find("span",{"class":"index"})
    s_index = s_index.get_text(strip=True)
    s_title = tds[0].find('span',{'class':'SingleLineText_text__HI_cb'})
    s_title = s_title.get_text(strip=True)
    s_price = tds[1].find("span",{"class":"SingleLinePrice_price__g_6VV"})
    s_price = s_price.get_text(strip=True)
    s_before = tds[2].find("span",{"class":"ModulePriceChange_amount__4QYMz"})
    s_before = s_before.get_text(strip=True)
    s_before1 = tds[2].find("span",{"class":"ModulePercent_module-percent__zioL9 ModulePercent_medium__OThzX ModulePercent_up__wFh0h"})
    s_before1 = s_before1.get_text(strip=True)
    s_amount = tds[5].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"})
    s_amount = s_amount.get_text(strip=True)
    s_total = tds[7].find("span",{"class":"SingleLineText_text__HI_cb"})
    s_total = s_total.get_text(strip=True)
    tds[7]
    # trs = s_tbody.find_all('tr')  # 100개 정보
    print(f"{s_index},{s_title},{s_price},{s_before},{s_before1},{s_price},{s_total}")
    print("-"*70)


# 1. requests
# 단점 : 자바스크립트로 구동되는 소스 가져올수 없다.
# requests정보가져오기 -> css문법변환 -> find,find_all()
# url = "https://www.melon.com/chart/index.htm"
# # User-Agent : Python-requests 정보
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료
# # css문법변환
# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법