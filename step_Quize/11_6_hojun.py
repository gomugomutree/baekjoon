import sys

n = int(sys.stdin.readline())

number = []
for _ in range(n):
    number.append(list(map(int, input().split())))
number.sort()
for i in number:
    print(i[0],i[1])




# sort 하면 해결......
# # print(number) # [['3', '4'], ['1', '1'], ['1', '-1'], ['2', '2'], ['3', '3']]
# number.sort(key=lambda x : x[0])
# # print(number) # [['1', '1'], ['1', '-1'], ['2', '2'], ['3', '4'], ['3', '3']]

# for i in range(len(number)-1):
#     # 앞의 숫자가 같고 뒤의 숫자가 뒤의 리스트 보다 크면 
#     if number[i][0] == number[i+1][0] and (int(number[i][1]) > int(number[i+1][1])):
#         # print(number[i]) # ['1', '1'],  ['3', '4']
#         # print(number[i][1]) # 1   4
#         number[i], number[i+1] = number[i+1] , number[i]

# # print(number) # [['1', '-1'], ['1', '1'], ['2', '2'], ['3', '3'], ['3', '4']]

# for i in number:
#     print(i[0],i[1])


# number.sort()
# print(number)