def main():
    H,W,T = map(int, input().split())
    s = [list(input()) for i in range(H)]
    import heapq
    l = 1
    r = T + 1

    sx=0
    sy = 0
    for i in range(H):
        for j in range(W):
            if s[i][j] == 'S':
                sx = i
                sy = j
                break


    while(l + 1 < r):
        q = []
        m = (l+r)//2
        q.append((0,sx,sy))
        ret = 0
        d = dict()
        d[(sx,sy)] = 0
        while(q):
            c,x,y = heapq.heappop(q)
            if s[x][y] == 'G':
                ret = c
                break
            else:
                for x2,y2 in ((x+1, y), (x,y+1),(x-1,y),(x,y-1)):
                    if 0<= x2 < H and 0 <= y2 < W:
                        k = 1
                        if s[x2][y2] == '#':
                            k = m
                        if (x2,y2) in d and d[(x2,y2)] <= c + k:
                            continue
                        d[(x2,y2)] = c + k
                        heapq.heappush(q,(c+k,x2,y2))
        if ret <= T:
            l = m
        else:
            r = m
        
    print(l)
main()    
