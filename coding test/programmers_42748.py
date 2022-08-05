def solution(array, commands):

    answer = []
    
    for command in commands:
        first = command[0] - 1
        end = command[1]
        point = command[2]
        
        cut = array[first:end]
        cut.sort()
        answer.append(cut[point-1])
        
    return answer