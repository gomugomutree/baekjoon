def solution(numbers, target):
    print(numbers, target)
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers=numbers[1:], target = target-numbers[0]) + solution(numbers=numbers[1:], target = target+numbers[0])


print(solution([1, 1, 1, 1, 1], 3))