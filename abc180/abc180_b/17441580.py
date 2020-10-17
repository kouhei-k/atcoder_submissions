import math
N = int(input())
x = list(map(int, input().split()))
k = sum(map(abs, x))

print(k)
print(math.sqrt(sum(map(lambda x: x**2, x))))
print(max(map(abs, x)))
