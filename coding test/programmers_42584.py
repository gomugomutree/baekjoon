def solution(prices):
    # 반환값도 같은 길이로 만든다.
    answer = [0] * len(prices)
    
    for idx in range(len(prices)):
        # 비교할 숫자를 넣는다.
        first = prices[idx] 
        
        # 시간 체크
        check = 0
        
        # 첫 숫자와 비교
        for i in range(idx+1, len(prices)):
            if first > prices[i]: # 가격 떨어지면
                answer[idx] = i - idx # 시간차이(index 차이) 넣기
                check = 0 
                break
            else:
                check += 1 # 초 진행
        
        # 끝까지 가격이 안 떨어지면 
        if check >= 1:
            # 비교하는 숫자랑 반환값이랑 index가 같다
            answer[idx] = check 
            
    return answer