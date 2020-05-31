N = int(input())
A = list(map(int, input().split()))
ans = 1
A.sort()
if A[0] == 0:
    print(0)
else:
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            print(-1)
            exit(0)
    print(ans)
