def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    
    # 정렬할때 각 수를 3번 곱해줘서 다시 정렬
    # 3자리 숫자까지만 비교해서 정렬해도 문제상 1000 이하 이므로
    # 모든 경우의 수로 비교 가능
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    
    # '0000' 일 경우를 대비
    if answer[0] == '0':
        answer = '0'
        
    return answer