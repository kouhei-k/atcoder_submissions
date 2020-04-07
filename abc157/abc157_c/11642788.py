N, M = map(int, input().split())
ans = [-1]*N

for i in range(M):
    s, c = map(int, input().split())
    if ans[s-1] > 0:
        if ans[s-1] == c:
            continue
        else:
            print(-1)
            exit(0)
    else:
        if s == 1 and c == 0 and N != 1:
            print(-1)
            exit(0)
        ans[s-1] = c

for i in range(N):
    if ans[i] == -1:
        if i == 0 and N != 1:
            ans[i] = 1
        else:
            ans[i] = 0

print("".join(map(str, ans)))
