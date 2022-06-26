# 	10809번
x = input()
for i in range(ord('a'), ord('z')+1):
    if chr(i) in x:
        for idx, j in enumerate(list(x)):
            if j == chr(i):
                print(idx, end=' ')
                break
    else:
        print(-1, end=' ')
