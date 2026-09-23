from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

browser = webdriver.Chrome()
url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
browser.get(url)
time.sleep(3)

elem = browser.find_elements(By.CSS_SELECTOR,"tbody tr")
for el in elem:
    print(el.text)