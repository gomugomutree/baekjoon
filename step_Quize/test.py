lst = [[2, 1], [3, 4], [1, 3], [3, 2], [1, 2]]
lst.sort()
print(lst)
lst.sort(key=lambda x:x[1])
print(lst)
lst.sort(key=lambda x: (x[1], x[0]))
print(lst)
lst.sort(key=lambda x: x[0])
print(lst)