N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    tmp = 1/N
    k = i
    count = 0
    while(k < K):
        k *= 2
        count += 1

    tmp /= 2**count

    ans += tmp
print(ans)
