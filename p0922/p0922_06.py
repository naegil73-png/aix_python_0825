# import requests
# from bs4 import BeautifulSoup

# url = "https://www.google.com/"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()

# # 타이틀을 출력, google정보 출력

# soup = BeautifulSoup(res.text,'lxml')
# print("-"*50)
# print(soup.title.get_text)

# print(soup.find("a", {"class":"bg_6"}).get_text())

import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# 타이틀을 출력, google정보 출력

soup = BeautifulSoup(res.text,'lxml')
print("-"*50)
print(soup.title.get_text())                                                                                                                                  

print(soup.find("strong", {"class":"cnf_news_title"}).get_text())

