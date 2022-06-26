# 1712번 
n = list(map(int, input().split()))
if n[1] >= n[2]:
    print(-1)
else:
    print(int(n[0]/(n[2]-n[1]))+1)
