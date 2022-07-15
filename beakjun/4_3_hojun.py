numbers = []
for i in range(3):
    numbers.append(int(input()))
numbers_sum = str(numbers[0] * numbers[1] * numbers[2])
a = list(map(str, list(range(10))))
for i in a:
    print(numbers_sum.count(i))
