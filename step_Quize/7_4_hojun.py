# 2869

n = input().split()
n = list(map(int, n))
k = (n[0] - n[1])
if  (n[2] -n[0]) % (n[0] - n[1]) == 0:
    print(int( (n[2] + k - n[0]) / k))
else:
    print(int( (n[2] + k - n[0]) / k) +1)
