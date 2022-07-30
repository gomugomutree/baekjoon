def solution(s):
    answer = False
    a = 0

    for i in s:
        if a  < 0:
            return False
        elif i == '(':
            a += 1
        else:
            a -= 1
            
    if a == 0:
        answer = True
    return answer