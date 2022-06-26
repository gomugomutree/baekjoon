import sys

# n = list(sys.stdin.readline())
n = list(input())
n.sort(reverse=True)
print(''.join(n))