N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())
size = [[P, Q, R], [P, R, Q], [Q, P, R], [Q, R, P], [R, P, Q], [R, Q, P]]
ans = 0
for x in size:
    ans = max(ans, (N//x[0]) * (M // x[1]) * (L//x[2]))

print(ans)
