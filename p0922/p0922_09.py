# import requests
# from bs4 import BeautifulSoup

# url = "https://www.melon.com/chart/index.htm"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료

# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법

# #파일저장
# # with open('melon1.html','w',encoding='utf-8') as f:
# #     f.write(res.text)

# # with open('melon2.html','w',encoding='utf-8') as f:
# #     f.write(soup.prettify())
# #
# print("-"*50)
# # 1개 find, 여러개 find_all
# s_tbody = soup.tbody
# trs = s_tbody.find_all("tr")  #타입:list
# for tr in trs:
#     tds = tr.find_all("td")
#     try:
#         print("순위 : ",tds[1].find("span",{"class":"rank"}).get_text()+"위")
#         print("링크 :",tds[3].find("img")['src'])  #[],attrs
#         s_as = tds[5].find_all("a")
#         print("제목명: ",s_as[0].get_text())  #노래제목
#         print("가수명 :",s_as[1].get_text())  #가수명
#         print("앨범명 :",tds[6].find("a").get_text())  #앨범명
#         print("-"*30)
#     except Exception as e:
#         print(e)

# print("완료!!")

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.melon.com/chart/index.htm"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료

# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법 

# #파일저장
# # with open('melon1.html','w',encoding='utf-8') as f:
# #     f.write(res.text)

# # with open('melon2.html','w',encoding='utf-8') as f:
# #     f.write(soup.prettify())
# #
# print("-"*50)
# # 1개 find, 여러개 find_all
# s_tbody = soup.tbody # (소스를 잘 살펴봐야 함)웹페이지 소스에서 tbody부분을 s_tbody에 할당
# trs = s_tbody.find_all("tr")  #타입:list # tbody에서 순위태그인 tr태그를 모두 찾아서 trs에 할당하라
# for idx,tr in enumerate(trs): # trs에 있는 tr태그에 인덱스를 부여
#     tds = tr.find_all("td") # tr에 있는 칸(열)을 모두 찾아 tds에 할당
#     try:
#         print("순위 : ",tds[1].find("span",{"class":"rank"}).get_text()+"위") # 1번 열 태그에서 span태그에서 클래스가 rank인 것의 text를 구하라
#         img = tds[3].find("img")['src']
#         print("링크 :",img)  #[],attrs

#         #------------------------
#         # img정보를 가지고 호출을 다시해야 함. - img의 정보파일을 가져옴.
#         img_res = requests.get(img,headers=headers)
#         with open(f"melon_2026_{idx+1}.jpg","wb") as f:
#             f.write(img_res.content)
#         #------------------------
#         s_as = tds[5].find_all("a")
#         print("제목명: ",s_as[0].get_text())  #노래제목
#         print("가수명 :",s_as[1].get_text())  #가수명
#         print("앨범명 :",tds[6].find("a").get_text())  #앨범명
#         print("-"*30)
#     except Exception as e:
#         print(e)

# print("완료!!")


import requests
from bs4 import BeautifulSoup
import os

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법 

#파일저장
# with open('melon1.html','w',encoding='utf-8') as f:
#     f.write(res.text)

# with open('melon2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
#
print("-"*50)
# 1개 find, 여러개 find_all
s_tbody = soup.tbody # (소스를 잘 살펴봐야 함)웹페이지 소스에서 tbody부분을 s_tbody에 할당
trs = s_tbody.find_all("tr")  #타입:list # tbody에서 순위태그인 tr태그를 모두 찾아서 trs에 할당하라
for idx,tr in enumerate(trs): # trs에 있는 tr태그에 인덱스를 부여
    tds = tr.find_all("td") # tr에 있는 칸(열)을 모두 찾아 tds에 할당
    try:
        print("순위 : ",tds[1].find("span",{"class":"rank"}).get_text()+"위") # 1번 열 태그에서 span태그에서 클래스가 rank인 것의 text를 구하라
        img = tds[3].find("img")['src']
        print("링크 :",img)  #[],attrs

        #------------------------
        # img정보를 가지고 호출을 다시해야 함. - img의 정보파일을 가져옴.
        os.makedirs("./melon_img",exist_ok=True) # 해당폴더가 있으면 무시
        img_res = requests.get(img,headers=headers)
        with open(f"melon_img/2026_{idx+1}.jpg","wb") as f:
            f.write(img_res.content)
        #------------------------
        s_as = tds[5].find_all("a") # 1개칸(열에 2개 a태그 보유)에서 a태그를 모두 찾아라
        print("제목명: ",s_as[0].get_text())  #노래제목 # 찾은 태그에서 첫번째의 글을 표시
        print("가수명 :",s_as[1].get_text())  #가수명
        print("앨범명 :",tds[6].find("a").get_text())  #앨범명
        print("-"*30)
    except Exception as e:
        print(e)

print("완료!!")