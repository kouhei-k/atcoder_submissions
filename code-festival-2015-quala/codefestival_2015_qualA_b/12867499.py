N = int(input())
A = list(map(int, input().split()))
ans = 0
tmp = 1
for i in range(N-1, -1, -1):
    ans += tmp*A[i]
    tmp *= 2

print(ans)
