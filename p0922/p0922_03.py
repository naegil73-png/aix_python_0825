import requests

# res = requests.get("https://www.melon.com/chart/index.htm")
# res.raise_for_status()

# with open ("melon.hmtl", "w", encoding="utf8") as f:
#     f.write(res.text) #  406 Client Error: Not Acceptable for url


url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open ("melon2.html", "w", encoding="utf8") as f:
    f.write(res.text) #  406 Client Error: Not Acceptable for url

print("저장 완료")