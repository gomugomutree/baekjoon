k = int(input())
x = list(map(int, input().split()))
num = 0
def number(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1

for i in x:
    if i == 1:
        pass
    else:
        num += number(i)
print(num)
