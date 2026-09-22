import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

# 파일저장
# with open("melon1.html","w",encoding="utf-8") as f:
#     f.write(res.text)

soup = BeautifulSoup(res.text,'lxml')
print("-"*50)

s_tbody = soup.tbody
trs = s_tbody.find_all("tr",{"class":"lst50"}) #리스트 접근방법 : trs[i]
for i in range(50):
    tds = trs[i].find_all("td")
    rank = tds[1].find("span").get_text()
    src = tds[3].find("div")

    print(f"{i+1} : {rank}, {src}") 