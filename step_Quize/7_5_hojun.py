# 10250
roof  = int(input())
layer = []
num = []
for i in range(roof):
    cus = input().split()
    cus = list(map(int, cus))
    if cus[2] % cus[0] == 0:
        layer.append(cus[0])
        num.append(format(int(cus[2] / cus[0]), '02'))
    else:
        layer.append(cus[2] % cus[0])
        num.append(format(int(cus[2] / cus[0]) + 1, '02'))
[print(f'{layer[i]}{num[i]}') for i in range(roof)]



