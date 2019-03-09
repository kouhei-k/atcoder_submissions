N, A, B = map(int, input().split())

X = list(map(int, input().split()))
ans = 0
for i in range(N-1):
    dis = X[i+1] - X[i]
    if dis * A > B:
        ans += B
    else:
        ans += dis * A
print(ans)
