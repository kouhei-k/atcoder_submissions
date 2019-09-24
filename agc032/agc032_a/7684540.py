N = int(input())
b = list(map(int, input().split()))
ans = [-1]*N
for i in range(N):
    for j in reversed(range(len(b))):
        if b[j] == j+1:
            ans[i] = b.pop(j)
            break

if len(b) == 0:
    for i in reversed(range(N)):
        print(ans[i])
else:
    print(-1)
