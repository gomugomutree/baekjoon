k = int(input())
x = int(input())
num = []
for i in range(k, x+1):
    n = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                n += 1
                break
        if n == 0:
            num.append(i)
if len(num) > 0:
    print(sum(num))
    print(min(num))
else:
    print(-1)