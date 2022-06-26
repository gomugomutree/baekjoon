# 2839
k = int(input())
con = 0
if k < 10:
    if k == 5:
        print(1)
    elif k % 3 == 0 or k == 8:
        print(int(k/3))
    else:
        print(-1)
    exit()
while k >= 0:
    if k % 5 == 0:
        print(int(k / 5) + con)
        break
    k = k - 3
    con = con + 1
else:
    print(-1)