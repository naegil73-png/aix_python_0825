# arr = [1,2,3,4,5,6,7,8,9]

# # 2차원 리스트로 변환
# arr2 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# # 1차원 리스트를 2차원 리스트로 변환
# arr2 = []
# for i in range(0,9,3): # len(arr)해도 됨
#     arr2.append(arr[i:i+3])
# print(arr2)

# # 문자열을 3자리씩 끊어서 리스트에 저장
# aa = "abcdefabcdefabcdefabcdefabcdefabcdef"
# bb = []
# for i in range(0,len(aa),3):
#     bb.append(aa[i:i+3])
# print(bb)

# 1, 25까지 리스트를 생성하고
# 랜덤으로 리스트를 섞은 다음, 5개씩 2차원 리스트를 만드시오.

# import random
# alist = list(range(1,26))
# random.shuffle(alist)
# list2 = []
# for i in alist:
#     list2.append(alist[i:i+5])
# print(list2)
# print(alist)

# 위의 결과를 5개 단위로 줄바꿈해서 출력
import random
alist = list(range(1,26)) # 리스트 생성
random.shuffle(alist)
list2 = []
for i in range(0,25,5): # 원 리스트에서 새 리스트 생성 방법 설정
    list2.append(alist[i:i+5])
print(list2)