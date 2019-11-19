N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    if i >= K:
        ans += 1/N
    else:
        k = ((K-1)//i) + 1
        count = 0
        while(k/2**count > 1):
            count += 1

        ans += (1/N) * (1/2)**count
print(ans)
