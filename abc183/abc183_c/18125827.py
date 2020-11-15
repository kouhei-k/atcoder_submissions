from itertools import permutations
N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]

ans = 0
for x in permutations(range(1, N)):
    t = 0
    p = 0
    for y in x:
        t += T[p][y]
        p = y
    t += T[p][0]
    if t == K:
        ans += 1

print(ans)
