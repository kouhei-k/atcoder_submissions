N, K = map(int, input().split())
ans = 0
for ab in range(max(2, K+2), 2*N+1):
    tmp = 0
    if ab <= N+1:
        tmp = ab - 1
    else:
        tmp = N*2 - ab + 1

    cd = ab - K
    if cd <= N+1:
        tmp2 = cd - 1
    else:
        tmp2 = N*2 - cd + 1

    ans += max(0, tmp*tmp2)
    #print(ab, cd, tmp, tmp2)
print(ans)
