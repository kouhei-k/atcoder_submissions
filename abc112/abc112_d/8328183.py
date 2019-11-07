import fractions
N, M = map(int, input().split())

k = M // N + 1
ans = 1
for i in reversed(range(1, k+1)):
    if ans > i:
        break
    tmp = max(M - (N-1)*i, 1)
    if tmp % i == 0:
        ans = max(ans, i)

print(ans)
