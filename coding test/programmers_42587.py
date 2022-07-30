def solution(priorities, location):
    answer = 1

    max_ = max(priorities)
    point = priorities.index(max_)
    priorities[point] = 0
    print(answer, 'p', priorities,'\t', 'point', point)
    if location == point:
        return answer

    while True:
        point += 1
        if point == len(priorities):
            point = 0

        if priorities[point] == max(priorities):
            priorities[point] = 0
        else:
            max_ = max(priorities)
            point = priorities.index(max_)
            priorities[point] = 0

        answer += 1
        
        if location == point:
            print(answer, 'p', priorities,'\t', 'point', point)
            return answer
        print(answer, 'p', priorities,'\t', 'point', point)
        


# print(solution([1, 1, 9, 1, 1, 1],	0))
# print(solution([6, 4, 9, 2, 3, 3],	2))
print(solution([4, 9, 4, 4, 5, 4, 2, 9],	6))
