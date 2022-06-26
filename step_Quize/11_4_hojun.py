import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
print(round(sum(a)/n))
print(a[n//2])
num = []

# 최빈값 - 빈출
cnt_li = Counter(a).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

# 범위
print(a[-1] - a[0])


 