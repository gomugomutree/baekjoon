x = int(input())
n = 0
k = 1
while True:
    k = k + (6 * n)
    if x == 1:
        print(1)
        break
    if k < x & x <= (k + 6*(n+1)):
        print(n+2)
        break
    n += 1
