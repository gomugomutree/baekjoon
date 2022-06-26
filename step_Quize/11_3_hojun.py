# ## memory over issue
import sys

n = int(sys.stdin.readline())

count_list = [0]*10001

for _ in range(n):
    count_list[int(sys.stdin.readline())] += 1
for i in range(1, len(count_list)):
    for _ in range(count_list[i]):
        print(i)
