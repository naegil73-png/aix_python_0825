# a_arr = [1,5,10,20,90,100,7,2] # 자료 정렬
# a_arr.sort() # 원본이 변경되므로 원본 보존코자 한다면, 다른 리스트를 생성해야 함
# print(a_arr)

# a_arr = [1,5,10,20,90,100,7,2]
# a_arr2 = [*a_arr]
# a_arr.sort()
# print(a_arr)
# print(a_arr2)

# a_arr = [1,5,10,20,90,100,7,2]
# a_arr.pop(1)
# print(a_arr)

# a_arr = [1,5,10,20,90,100,7,2]
# del a_arr[1]
# print(a_arr)

# a_arr = [1,5,10,20,90,100,7,2]
# a_arr.remove(5) # remove는 삭제하고자 하는 값을 입력
# print(a_arr)

# aa = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# # aa를 만드는 명령구문

# a_arr = []
# for i in range(0,12,4):
#     a_arr.append(aa[i:i+4])
# print(a_arr)

# aa = list(range(1,26))
# for i in aa:
#     print(i, end = "\t")
#     print()

# # 위의 것을 5개씩 1줄로 표현하려면..
# aa = list(range(1,26))
# for i in aa:
#     if i%5 != 0:
#         print(i, end = "\t")
#     else:
#         print()

# # aa를 섞은 후 5개씩 1줄로 표현하려면..
# import random
# aa = list(range(1,26))
# new=[]
# random.shuffle(aa)

# for i in range(0,len(aa),5):
#     print(aa[i:i+5])
# print(aa)


# bingo 만들기, 입력한 숫자에 X표시되게 함
import random
a_arr = list(range(1,26))
random.shuffle(a_arr)
while True:
    print(" "*15,end = "")
    print(" [빙고게임]")
    print("-"*50)
    for i,v in enumerate(a_arr):
        if (i+1)%5 !=0:
            print(v,end ="\t")
        else:
            print(v)
    print("-"*50)
    num = int(input("원하는 번호를 입력하세요>>"))
    if num in a_arr:
        idx = a_arr.index(num) # a_arr에서 num의 위치를 반환. 즉, a_arr에서 num
        a_arr[idx] = "X"