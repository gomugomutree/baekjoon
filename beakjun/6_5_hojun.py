# 1157번
n = input().lower()
num = 0
while len(n) != 0:
    i = n.count(n[0])
    if num < i: 
        num = i
        key1 =n[0]
    elif num == i:
        key1 = '?'
    n = n.replace(n[0], '')
print(key1.upper())