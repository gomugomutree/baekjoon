import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
for i in range(n):
    print(a[i])
