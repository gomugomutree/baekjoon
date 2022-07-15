# 2775
t = int(input())
for _ in range(t):  
    f = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]
    for k in range(f):
        for i in range(1, num):
            f0[i] = f0[i] + f0[i-1]    
    print(f0[-1])