N, C, K = map(int, input().split())
T = [int(input()) for i in range(N)]
T.sort()
count = 0
ans = 0
start = 0
for i in range(N):
    if count < C:
        if count == 0:
            count += 1
            start = T[i]
        else:
            if T[i] <= start + K:
                count += 1
            else:
                ans += 1
                count = 1
                start = T[i]
    else:
        count = 1
        ans += 1
        start = T[i]

    if i == N - 1:
        ans += 1
print(ans)
