import sys

n = int(sys.stdin.readline())

n_list = [input() for _ in range(n)]

# 중복 삭제
n_list = list(set(n_list))

# 정렬
n_list.sort()

answer = []

# 길이 순서
for i in range(1, 51):
    for j in range(len(n_list)):
        if len(n_list[j]) == i:
            answer.append(n_list[j])

for i in answer:
    print(i)
