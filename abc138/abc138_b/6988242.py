N = int(input())
A = list(map(int, input().split()))

devider = 0

for i in range(N):
    devider += (1 / A[i])

ans = 1 / devider

print(ans)
