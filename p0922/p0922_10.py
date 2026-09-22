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

# 브라우저 열기
browser = webdriver.Chrome()
url = "http://www.naver.com"

# 1.naver페이지 열림.
browser.get(url)
# 브라우저의 위치값을 찾아서 클릭하기
elem = browser.find_element(By.ID,'query') # 하나 찾을 때는 element, 여러개는 elements
elem.click()
# 뉴스페이지 이동
elem.send_keys("뉴스")
elem.send_keys(Keys.ENTER)
time.sleep(3) # 페이지 이동 대기시간
elem2 = browser.find_element(By.CLASS_NAME,"sds-comps-text")
elem2.click()
input()

