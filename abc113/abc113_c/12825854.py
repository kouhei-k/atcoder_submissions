N, M = map(int, input().split())
PY = [tuple(list(map(int, input().split()))+[i]) for i in range(M)]
PY.sort(key=lambda x: x[1])
ans = ['']*M
P = [0]*N
for p, y, i in PY:
    ret = ''
    p -= 1
    P[p] += 1
    ret += '{:0=6}'.format(p+1)
    ret += '{:0=6}'.format(P[p])
    ans[i] = ret
print(*ans, sep='
')
