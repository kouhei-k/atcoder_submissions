def main():
    import collections
    import sys
    input = sys.stdin.buffer.readline
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    input = sys.stdin.readline
    S = [input() for i in range(H)]

    q = collections.deque()
    Ch -= 1
    Cw -= 1
    Dh -= 1
    Dw -= 1

    flag = True

    r = set()
    ss = []
    start = -1
    goal = -1
    # D = collections.defaultdict(int)
    D = dict()
    for i in range(H):
        for j in range(W):
            if (i, j) in r or S[i][j] == '#':
                continue
            q.append((i, j))
            ss.append(set([(i, j)]))
            r.add((i, j))
            L = len(ss)
            D[(i, j)] = L-1
            while(q):
                x, y = q.popleft()
                for k, l in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if 0 <= k <= H-1 and 0 <= l <= W-1 and S[k][l] != '#' and (k, l) not in r:
                        r.add((k, l))
                        D[(k, l)] = L - 1
                        q.append((k, l))
                        ss[-1].add((k, l))
            if start == -1 and (Ch, Cw) in ss[-1]:
                start = L - 1
            if goal == -1 and (Dh, Dw) in ss[-1]:
                goal = L - 1

    if D[Ch, Cw] == D[(Dh, Dw)]:
        print(0)
        exit(0)

    G = [set() for i in range(len(ss))]
    for id, X in enumerate(ss):
        for x, y in X:
            for i in range(x-2, x+3):
                if 0 <= i <= H-1:
                    for j in range(y-2, y+3):
                        if 0 <= j <= W-1:
                            if S[i][j] != '#' and D[(i, j)] != id:
                                G[id].add(D[(i, j)])

    r = set()
    r.add(start)
    q.append((start, 0))
    while(q):
        x, c = q.popleft()
        if x == goal:
            print(c)
            flag = False
            break
        for y in G[x]:
            if y in r:
                continue
            else:
                r.add(y)
                q.append((y, c+1))
    # print(G)
    if flag:
        print(-1)


main()
