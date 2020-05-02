A, B, N = map(int, input().split())
l = -1
r = N
# ans = 0
# for i in range(1, N+1):
#     ans = max(ans, (A*i)//B - (A*(i//B)))
k = min(B-1, N)
ans2 = (A*k)//B - (A*(k//B))

print(ans2)
