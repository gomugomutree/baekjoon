# import numpy as np
# k= int(input())
# stop =0
# while k != stop:
#     n = input()
#     line = float(n.split(' ')[0])
#     score = n.split(' ')[1:]
#     score = np.array(n.split(' ')[1:]).astype(float)
#     print(format(round(len(score[score.mean()< score])/line*100, 3),".3f")+'%')

k= int(input())
stop =0
while k != stop:
    n = input()
    line = int(n.split(' ')[0])
    score = list(map(int, n.split(' ')[1:]))
    num = 0
    for i in score:
        if i > (sum(score)/line):
            num += 1
    print(format(round((num/line)*100, 3),".3f")+'%')
    stop += 1
