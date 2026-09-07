# 파일복사하기
import os

rf = open("C:\\aaa\\1.jpg",'rb') # 파일을 읽을 때는 'rb'(바이너리 파일로 읽음), 글은 'r'
wf = open("C:\\aaa2\\2.jpg",'wb') # 파일을 쓸 때는 'rw'

while True:
    fdata = rf.read(1) # (1) : 1바이트 단위로 읽음
    if not fdata: break # 파일이 없으면 멈춤
    wf.write(fdata) # fdata를 쓴다.

rf.close()
wf.close()

print('이미지파일이 복사되었습니다.')

rf = open("C:\\aaa\\2.jpg",'rb')
wf = open("C:\\aaa2\\2.jpg",'wb')

while True:
    fdata = rf.read(1)
    if not fdata: break
    wf.write(fdata)

rf.close()
wf.close

print('이미지파일이 복사되었습니다.')