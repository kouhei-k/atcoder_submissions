N = int(input())
A = list(map(int, input().split()))
ans = [[0, 0] for i in range(N)]
for i in range(N):
    ans[i] = [A[i], i]

ans.sort(key=lambda x: x[0])
ans_str = [str(ans[i][1] + 1) for i in range(N)]
print(" ".join(ans_str))
