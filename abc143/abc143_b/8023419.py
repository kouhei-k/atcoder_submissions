N = int(input())
d = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        else:
            ans += d[i] * d[j]

print(ans)
