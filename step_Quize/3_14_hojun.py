n = int(input())
first_n = n
cycle = 0
while True:
    if n < 10:
        n = n*10 + n
    else:
        n = (n%10)*10 + (int((n/10))+(n%10))%10
    cycle += 1
    if n == first_n:
        break
print(cycle)