def solution(participant, completion):
    answer = ''
    # dictionary 형태로 값을 받아온다.
    dic = { s: 0 for s in participant}

    for i in participant:
       dic[i] += 1
    
    for i in completion:
        dic[i] -= 1
    
    for i in dic:
        if dic[i] > 0:
            answer = i        
        
    return answer
