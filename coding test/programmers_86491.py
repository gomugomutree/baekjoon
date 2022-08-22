def solution(sizes):
    answer = 0
    for i in sizes:
        i.sort(reverse=True)
    sizes.sort(reverse=True)
    # print(sizes)
    w = sizes[0][0]
    # print(w)
    sizes.sort(key= lambda x :x[1], reverse=True)
    h = sizes[0][1]
    answer = w * h
    return answer