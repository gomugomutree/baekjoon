def solution(nums):
    answer = len(nums)/2
    
    nums = len(list(set(nums)))
    if answer < nums:
        return answer
    else:
        return nums
    