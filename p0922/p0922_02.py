import requests

# res = requests.get("https://www.google.com/") # 구글의 소스를 다 가져온다 -> 소스 가져오는 것은 불법? 잘 활용해야..
# res = requests.get("https://www.naver.com/") # 네이버 소스를 다 가져온다
# print("응답코드:",res.status_code) # 응답코드를 가져옴
# print("html소스 : ",res.text) # 텍스트 정보를 알수 있음 
# # http에 요청 시 f12눌러서 network확인하면 : 100 : 요청처리, 200: 처리 성공, 300: 추가행동, 400: 클라이언트 오류, 요청에러?, 500: 서버에러(개발자오류)

res = requests.get("https://www.melon.com/") # 멜론의 소스를 다 가져온다 -> 막은 경우, 400번대 오류
res.raise_for_status() #에러나면 종료하는 명령문
print(res.text) # 텍스트 정보를 알수 있음 
print("응답코드:",res.status_code) # 응답코드를 가져옴
print("프로그램을 종료합니다.")