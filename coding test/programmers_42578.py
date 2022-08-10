import math
def solution(clothes):
    answer = 1
    dic = {}

    for key in clothes:
        dic[key[-1]] = 0
    print(dic)
        
    for key in clothes:
        if key[-1] in dic:
            dic[key[-1]] += 1
    
    if len(dic) == 1:
        return len(clothes)
    else:
        for value in dic.values():
            answer *= (value +1)
        
    return answer -1