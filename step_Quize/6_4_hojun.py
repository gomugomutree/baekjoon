# 2675번
a = int(input())
while a !=0:
    x = input()
    n, y = x.split(" ")
    y_list = list(y)
    for i in y_list:
        print(i*int(n), end='')
    print()
    a -= 1 