# alarm time - 45 minute
# 10 10  ->  9 25

current_alarm = input()
H, M = current_alarm.split(' ')
H = int(H)
M = int(M)
if M < 45:
    H = H - 1
    M = 15 + M
    if H < 0:
        H = 23
else:
    M = M - 45
print(f'{H} {M}')