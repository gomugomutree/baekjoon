def pri_max(temp):
    max = 0
    for i in range(len(temp)):
        if temp[i][0] > max:
            max = temp[i][0]
    return max

        
def solution(priorities, location):
    answer = 1
    
    temp = []
    pri_len = len(priorities)
    pri_list = []
    
    for index, pri in enumerate(priorities):
        temp.append([pri, index])
    
    check = 0
    while len(pri_list) < pri_len:
        print(temp)
        if temp[0][0] == pri_max(temp):
            k = temp.pop(0)
            pri_list.append(k)
        else:
            k = temp.pop(check)
            temp.append(k)
        
    for i in range(len(pri_list)):
        if pri_list[i][1] == location:
            return i
