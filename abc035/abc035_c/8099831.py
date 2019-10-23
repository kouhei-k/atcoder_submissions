N, Q = map(int, input().split())
arr = [0]*(N+1)
field = [0]*(N+1)
for i in range(Q):
    a, b = map(int, input().split())
    arr[a-1] += 1
    arr[b] -= 1
ans = [0]*N
for i in range(N):
    field[i+1] = field[i]+arr[i]
    ans[i] = field[i+1] % 2

print("".join(map(str, ans)))
