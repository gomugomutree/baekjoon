a = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
x = input()
num = 0
for i in x:
    for idx, j in enumerate(a):
        if i in j:
            num = idx + 3 + num
print(num)