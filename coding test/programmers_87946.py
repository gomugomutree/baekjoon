import itertools

def solution(k, dungeons):
    answer = 0
    arr = list(itertools.permutations(dungeons, len(dungeons)))
    # print(arr)
    for dun in arr:
        check = 0
        temp = k
        for d_in, d_out in dun:
            if d_in <= temp:
                temp -= d_out
                check += 1
                # print(temp)
                
        if check > answer:
            answer = check
    return answer