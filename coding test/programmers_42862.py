def solution(n, lost, reserve):
    answer = 0
    # 전체 학생번호 : index
    # 체육복 보유수 : value
    student = [1] * (n+2)
    # 0번 학생과 여분 학생번호는 0
    student[0] = 0
    student[-1] = 0
    # print(student)

    # 도난당한 학생의 채육복 -1
    for i in lost:
        student[i] -= 1
        
    # 여벌 채육복이 있는 학생 채육복 +1
    for i in reserve:
        student[i] += 1
        
    # 빌려주기
    for i in range(1, len(student)-1):
        if student[i] == 0 and student[i-1] == 2:
            student[i] = 1
            student[i-1] = 1
            
        elif student[i] ==0 and student[i+1] ==2:
            student[i] = 1
            student[i+1] = 1

    for i in range(1, len(student)-1):
        if student[i] >= 1:
            answer += 1
            
    return answer
