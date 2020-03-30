N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

sa1 = [0]*(N+1)
sa2 = [0]*(N+1)

for i in range(N):
    sa1[i+1] = sa1[i] + A1[i]
    sa2[i+1] = sa2[i] + A2[i]

ans = 0
for i in range(1, N+1):
    ans = max(ans, sa1[i] + sa2[N] - sa2[i-1])

print(ans)
