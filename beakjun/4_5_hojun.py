n = int(input())
numbers = list(map(int, input().split()))
new_sum = 0
for i in range(n):
    new_sum = numbers[i]/max(numbers) + new_sum
print(round((new_sum/n * 100), 6))