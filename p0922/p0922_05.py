# import requests
# from bs4 import BeautifulSoup

# url = "https://n.news.naver.com/article/094/0000013820?cds=news_media_pc&type=editn"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml") # res.text를 css를 사용할 수 있는 lxml으로 변경 (변경대상, 변경방식?)
# # print("-"*50)
# # print("a 태그:", soup.a) # soup에서 a태그를 찾아줘
# # print("a 태그:", soup.a['href']) # soup에서 a태그에서 href를 찾아줘(속성하나만 요청 시 [속성]으로 하면 됨)
# # print("a 태그:", soup.a.attrs) # soup에서 a태그 속성의 모든 값
# # # 파일을 전체 저장 : res.text
# # # 필요한 부분만 저장 : 파싱 후 원하는 부분 저장
# # # print("뉴스랭킹:", soup.rank) # soup에서 주요 뉴스를 찾아줘라는 명령도 가능

# # print("title 제목:", soup.title) # soup에서 title태그를 찾아줘
# # print("title 제목:", soup.title.get_text()) # soup에서 title에서 텍스트만

# print(soup.prettify()) # 코드가 정렬되어 저장이 됨 - 저장 시 가급적 이렇게

import requests # 웹에서 데이터 가져오기 라이브러리
from bs4 import BeautifulSoup # 태그해석, 파싱 라이브러리

url = "https://www.melon.com/chart/index.htm"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml') # res를 text로 읽은 다음, lxml로 변환하라(파싱에 편리한 언어)
print(soup.prettify())

# 태그로 찾는 방법, 속성1개, 속성 모두 찾soup = BeautifulSoup(res.text,'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.div.attrs)
# print(soup.tbody)

# # id, class로 찾는 방법

# print(soup.find("div",{"id":"header"})) # soup에서 < >에서 div를 찾고, 중괄호는 id가 header인 것을 찾아라
# print(soup.find("div",{"id":"util_menu"})) # soup에서 < >에서 div를 찾고, 중괄호는 id가 util_menu인 것을 찾아라
print(soup.find("div",{"class":"lst50"})) # soup에서 < >에서 div를 찾고, 중괄호는 class가 lst50인 것을 찾아라
print(soup.find("div",{"class":"wrap t_right"})) # soup에서 < >에서 div를 찾고, 중괄호는 class가 lst50인 것을 찾아라
# 곡목록 전체를 가져오려고 함
print(soup.find("input",{"class":"input_check d_checkall"})['title']) # soup에서 < >에서 div를 찾고, 중괄호는 class가 lst50인 것을 찾아라