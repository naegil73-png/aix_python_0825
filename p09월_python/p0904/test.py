# with open("C:\\aaa\\test2.txt",'w',encoding='utf-8') as f:
#     while True:
#         line = input("입력사항:")
#         if line != "":
#             f.writelines(line+'\n')
#         else:
#             break
# print("파일이 저장되었습니다.")

# stu = []
# with open("C:\\aaa\\test2.txt",'r',encoding='utf-8') as f:
#     while True:
#         line = f.readline()
#         if line == "": break
#         line = line.strip()
#         print(line)

#         arr = line.split(',')
#         for i, v in enumerate(arr):
#             if i>=2 and i <= 5:
#                 arr[i] = int(v)
#             if i == 6:
#                 arr[i] = float(v)
#         stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})
#     print(stu)








# with open("C:\\aaa\\test2.txt",'w',encoding='utf-8') as f:
#     while True:
#         line = input("입력사항:")
#         if line != "" : 
#             f.writelines(line+'\n')
#         else: break
#     print("파일이 저장되었습니다.")


with open("C:\\aaa\\test2.txt",'r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line == "": break
        line = line.strip()
        print(line)