
k = 1
n = 0
a =0
b =0
x = int(input())
while True:
    n = k + n
    if x <= n:
        b = n - x + 1
        a = k - b + 1
        if k % 2 == 0:
            print(f'{a}/{b}')
            break
        else:
            print(f'{b}/{a}')
            break
    k += 1
