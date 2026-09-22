import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

soup = BeautifulSoup(res.text,'lxml')
s_tbody = soup.tbody

trs = s_tbody.find_all("tr",{"class":"1st50"})
for i in trs:
    tds = trs[i].find_all("td")
    title = tds[5].find("div")['title']

    print(title)