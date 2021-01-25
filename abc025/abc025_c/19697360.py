b = [list(map(int, input().split())) for i in range(2)]
c = [list(map(int, input().split())) for i in range(3)]
d = dict()
G = '0'*9

def solve(G):
    # print(G)
    if G in d:
        return(d[G])
    
    s= set()
    id = 0
    for i in range(9):
        if G[i] == '0':
            s.add(i)
    ret = 0
    if len(s) == 0:
        for i in range(2):
            for j in range(3):
                if G[i*3 + j] == G[i*3+j+3]:
                    ret += b[i][j]
                else:
                    ret -= b[i][j]
        for i in range(3):
            for j in range(2):
                if G[i*3+j] == G[i*3+j+1]:
                    ret += c[i][j]
                else:
                    ret -= c[i][j]
        d[G] = ret
        return(ret)
    else:
        g = list(G)
        if len(s) % 2 == 1:
            ret = -10**3
            for j in s:
                g[j] = '1'
                ret = max(ret, solve(''.join(g)))
                g[j] = '0'
        else:
            ret = 10**3
            for j in s:
                g[j] = '2'
                ret = min(ret, solve(''.join(g)))
                g[j] = '0'
        d[G] = ret
        return(ret)
X = sum( sum(b[i][j] for j in range(3)) for i in range(2)) + sum(sum(c[i][j] for j in range(2)) for i in range(3))
ans = solve(G)
print((ans+X)//2)
print((X - ans) // 2)
