import requests

res = requests.get("http://www.google.com")
res.raise_for_status() # 에러코드시 프로그램 종료
print(res.text) # html모드 소스 가져오기
print(len(res.text))

# 파일로 저장하기
with open("google1.html",'w',encoding='utf-8') as f:
    f.write(res.text) # 

print("파일저장 완료")