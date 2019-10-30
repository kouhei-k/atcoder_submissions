N = int(input())
K = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += 2 * min(abs(K-x[i]), x[i])
print(ans)
