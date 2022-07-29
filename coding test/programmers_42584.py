def solution(prices):
    answer = []
    
    for  _ in range(len(prices)):
        # 리스트 첫 숫자 
        first = prices.pop(0)
        
        # 시간 체크
        check = 0
        
        # 첫 숫자와 비교
        for i in range(len(prices)):
            if first > prices[i]: # 가격 떨어지면
                answer.append(i+1)
                check = 0
                break
            else:
                check += 1 # 초 진행
        
        # 끝까지 가격이 안 떨어지면 
        if check >= 1:
            answer.append(check)
    # 마지막 가격 
    answer.append(0)

    return answer