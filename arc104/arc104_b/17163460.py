import math
N, S = input().split()
N = int(N)
D = dict()

ans = 0
for i in range(N):
    D['A'] = 0
    D['T'] = 0
    D['C'] = 0
    D['G'] = 0
    for j in range(i, N):
        D[S[j]] += 1
        if D['A'] == D['T'] and D['C'] == D['G']:
            ans += 1


print(ans)
