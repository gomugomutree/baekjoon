def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5] * 2000
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    count1, count2, count3 = 0, 0, 0
    for i in range(len(answers)):
        if num1[i] == answers[i]:
            count1 += 1
        if num2[i] == answers[i]:
            count2 += 1
        if num3[i] == answers[i]:
            count3 += 1
    score = [count1, count2, count3]
    # print(score)
    best = max(score)
    for i in range(len(score)):
        if best == score[i]:
            answer.append(i+1)
    return answer