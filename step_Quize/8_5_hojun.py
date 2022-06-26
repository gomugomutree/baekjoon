numbers = []
def find_sosu(x):
    if x ==1:        
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True	

for i in range(2, 246912):
    if find_sosu(i):
        numbers.append(i)

numbers_count = []
while True:
    n = int(input())
    num_count =0
    if n == 0:
        break
    for i in numbers:
        if n < i <= 2*n:
            num_count +=1
        elif i > 2*n:
            break
    numbers_count.append(num_count)

for i in numbers_count:
    print(i)


    