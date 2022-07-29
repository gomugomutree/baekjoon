import sys
import collections

numbers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]

# 행 중 1 자리만 비어 있는 숫자 채우기
for row_num in range(len(numbers)):
    if numbers[row_num].count(0) == 1:
        zero_index = numbers[row_num].index(0)
        numbers[row_num][zero_index] = 45 - sum(numbers[row_num])
        # print(row)

# 열 중 1 자리만 비어 있는 숫자 채우기
for column_num in range(len(numbers)):
    column_list = []
    for row in range(len(numbers)):
        column_list.append(numbers[row][column_num])
    # 1 열씩 리스트로 받아온다.
    if column_list.count(0) == 1:
        numbers[column_list.index(0)][column_num] = 45 - sum(column_list)

# 가운데 빈곳 채우기
for i in [1, 4, 7]:
    for j in [1, 4, 7]:
        if numbers[i][j] == 0:
            numbers[i][j] = 45 - int(numbers[i-1][j-1] + numbers[i-1][j] + numbers[i-1][j+1] 
                                   + numbers[i][j-1] +                     numbers[i][j+1]
                                   + numbers[i+1][j-1] + numbers[i+1][j]  + numbers[i+1][j+1])

for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i][j], end=" ")
    print()

# [[1, 3, 5, 4, 6, 9, 2, 7, 8], 
#  [7, 8, 2, 1, 0, 5, 6, 0, 9],   1,1   1,4   1,7
#  [4, 6, 9, 2, 7, 8, 1, 3, 5], 
#  [3, 2, 1, 5, 4, 6, 8, 9, 7], 
#  [8, 0, 4, 9, 1, 3, 5, 0, 6],   4,1   4,4   4,7
#  [5, 9, 6, 8, 2, 7, 4, 1, 3], 
#  [9, 1, 7, 6, 5, 2, 3, 8, 4], 
#  [6, 0, 3, 7, 0, 1, 9, 5, 2],   7,1   7,4   7,7
#  [2, 5, 8, 3, 9, 4, 7, 6, 1]]