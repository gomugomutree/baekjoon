a = set(range(1, 10001))
b = set()
for i in range(1, 10001):
    for j in str(i):
        i = i + int(j)
    b.add(i)
k = sorted(a-b)
for itr in k:
    if itr == len(k)-1:
        print(k, end='')
    else:
        print(k)