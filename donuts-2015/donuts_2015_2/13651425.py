from itertools import combinations
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [[0, set()] for i in range(M)]
for i in range(M):
    b, c, *I = map(int, input().split())
    B[i][0] = b
    B[i][1] |= set(I)
ans = 0
for x in combinations(range(N), 9):
    score = 0
    s = set()
    for j in x:
        score += A[j]
        s.add(j+1)
    if len(s) != 9:
        continue
    for b, ss in B:
        if len(ss & s) >= 3:
            score += b
    ans = max(ans, score)
print(ans)
