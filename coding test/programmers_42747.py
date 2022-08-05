def solution(citations):
    lenght = len(citations)
    result = []
    
    # [2, 2] 일 경우를 위해 lenght+1
    for h in range(1, lenght+1):
        # 하나씩 비교해서 
        up = list(map(lambda x : True if x >=h else False , citations))
        # h 이상의 인용 논문 개수가 h 개 이상인 것 
        # and 이상인 개수가 이하인 개수보다 많거나 같을 때 
        if (sum(up) >= h) and (sum(up) >= (lenght - sum(up))):
            result.append(h)
    
    # 전부다 0 인 경우
    if len(result) == 0:
        result.append(0)
    
    return max(result)
            