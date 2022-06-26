import sys

n = int(sys.stdin.readline())

number = []
for _ in range(n):
    number.append(list(map(int, sys.stdin.readline().split())))
number.sort(key=lambda x : (x[1], x[0]))

for i in number:
    print(i[0], i[1])


# 이게 문제가 된다. 
# 입력
# 5
# -1 1
# -2 1
# -3 1
# -5 1
# -6 1
# 출력 
# -6 1
# -5 1
# -3 1
# -2 1
# -1 1
