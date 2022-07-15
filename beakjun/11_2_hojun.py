import sys

n = int(sys.stdin.readline())

list_num = []
for _ in range(n):
    list_num.append(int(sys.stdin.readline()))

list_num.sort()
for i in list_num:
    print(i)