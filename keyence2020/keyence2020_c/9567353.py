N, K, S = map(int, input().split())

ans = [0]*N
T = 10**9
if T == S:
    T = 10**9 - 1
for i in range(N):
    if i < K:
        ans[i] = S
    else:
        ans[i] = T
print(" ".join(map(str, ans)))
