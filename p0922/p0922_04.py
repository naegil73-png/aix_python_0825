# import requests # 웹사이트에 접근을 할 수 있게 만드는 라이브러리, beautifulsoup4는 html, xml 문서를 쉽게 파싱할 수 있는 라이브러리(문자데이터)

# res = requests.get('http://www.google.com') # 구글사이트 소스에 접근하여 가져와라
# res.raise_for_status() #에러시 종료 -> 브라우저가 아닌 프로그램 접근 시 막아 놓은 사이트도 있음(user-agent를 통해서 접근방법 등 사용자 정보를 통해 걸러냄)
# print(res.status_code) # 요청한 것에 대한 상태(처리상태)를 나타내줘

# print(res.text) # 읽은 소스코드를 텍스트로 표시해라

# with open("google..html",'w',encoding='utf-8') as f: 
#     f.write(res.text)


#  프로그램 접근 시 프로그램 접근 정보가 나옴
# import requests # 웹사이트에 접근을 할 수 있게 만드는 라이브러리, beautifulsoup4는 html, xml 문서를 쉽게 파싱할 수 있는 라이브러리(문자데이터)

# res = requests.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/') # 구글사이트 소스에 접근하여 가져와라
# res.raise_for_status() #에러시 종료 -> 브라우저가 아닌 프로그램 접근 시 막아 놓은 사이트도 있음(user-agent를 통해서 접근방법 등 사용자 정보를 통해 걸러냄)
# print(res.status_code) # 요청한 것에 대한 상태(처리상태)를 나타내줘

# print(res.text) # 읽은 소스코드를 텍스트로 표시해라

# with open("google..html",'w',encoding='utf-8') as f: 

# f.write(res.text)


# # 프로그램 접근하지만, 웹으로 접근하는 것으로 조정하는 명령어
# import requests

# # res = requests.get("https://www.melon.com/chart/index.htm")
# # res.raise_for_status()

# # with open ("melon.hmtl", "w", encoding="utf8") as f:
# #     f.write(res.text) #  406 Client Error: Not Acceptable for url

# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/" # 나의 User-agent를 url로 바꿔주는 사이트 -> 웹으로 접속 후 agent를 복사해서 사용하면 됨
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()

# with open ("melon2.html", "w", encoding="utf8") as f:
#     f.write(res.text) #  406 Client Error: Not Acceptable for url

# print("저장 완료")


# 전체 웹화면에서 원하는 부분만 선택하려면 파싱해야 함
import requests
from bs4 import BeautifulSoup # html로 파싱

# res = requests.get("https://www.melon.com/chart/index.htm")
# res.raise_for_status()

# with open ("melon.hmtl", "w", encoding="utf8") as f:
#     f.write(res.text) #  406 Client Error: Not Acceptable for url

url = "https://www.melon.com/chart/index.htm"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open ("melon1.html", "w", encoding="utf8") as f:
    f.write(res.text) #  406 Client Error: Not Acceptable for url

print("저장 완료") 
# melon.html문서를 alt+b로 열면, 깨져서 나오지만, css가 적용되지 않아서 그런 것 
# 링크에 딕렉토리 주소 <link rel="stylesheet" href="/resource/style/web/common/melonweb_layout.css?tm=20260813" type="text/css" />가 있으면,
# 맨 앞에 http://www.melon.com를 추가해주면 그대로 나옴


url = "https://www.naver.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open ("naver1.html", "w", encoding="utf8") as f:
    f.write(res.text) #  406 Client Error: Not Acceptable for url

print("저장 완료") 
# melon.html문서를 alt+b로 열면, 깨져서 나오지만, css가 적용되지 않아서 그런 것 
# 링크에 딕렉토리 주소 <link rel="stylesheet" href="/resource/style/web/common/melonweb_layout.css?tm=20260813" type="text/css" />가 있으면,
# 맨 앞에 http://www.melon.com를 추가해주면 그대로 나옴

