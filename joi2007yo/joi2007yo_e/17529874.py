a, b, c = map(int, input().split())
N = int(input())
ijkr = [tuple(map(int, input().split())) for i in range(N)]

ans = [2]*(a+b+c)
for i in range(N):
    for i, j, k, r in ijkr:
        if r == 1:
            ans[i-1] = 1
            ans[j-1] = 1
            ans[k-1] = 1
        else:
            if ans[i-1] == 1 and ans[j-1] == 1:
                ans[k-1] = 0
            elif ans[i-1] == 1 and ans[k-1] == 1:
                ans[j-1] = 0
            elif ans[j-1] == 1 and ans[k-1] == 1:
                ans[i-1] = 0
print(*ans, sep='
')
