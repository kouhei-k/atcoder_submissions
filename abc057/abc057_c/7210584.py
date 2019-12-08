import math
N = int(input())

divisors = []
i = 1
while i <= math.sqrt(N):
    if N % i == 0:
        divisors.append([i, int(N/i)])
    i += 1
ans = N
for i in divisors:
    if max(i) < ans:
        ans = max(i)

print(len(str(ans)))
