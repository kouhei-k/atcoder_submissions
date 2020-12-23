def main():
    import sys
    import collections

    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    a = ''.join(a)

    d = dict()
    sx = 0
    sy = 0
    gx = 0
    gy = 0
    d['.'] = set()
    d['S'] = set()
    for i in range(H):
        for j in range(W):
            A = a[i*W+j]
            if A == 'S':
                sx = i
                sy = j
            elif A == 'G':
                gx = i
                gy = j
            elif A == '#':
                continue
            elif A != '.':
                if A not in d:
                    d[A] = set()
                d[A].add((i, j))
    q = collections.deque()
    q.append((sx, sy))
    s = set()
    r = [0]*(W*H)
    r[sx*W+sy] = 0

    while(q):
        x, y = q.popleft()
        if x == gx and y == gy:
            print(r[x*W+y])
            exit(0)
        else:
            A = a[x*W+y]
            c = r[x*W+y]
            while(d[A]):
                x2, y2 = d[A].pop()
                if r[x2*W+y2]:
                    continue
                else:
                    r[x2*W+y2] = c+1
                    q.append((x2, y2))
            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= x2 < H and 0 <= y2 < W:
                    if r[x2*W+y2]:
                        continue
                    else:
                        if a[x2*W+y2] == '#':
                            continue
                        else:
                            q.append((x2, y2))
                            r[x2*W+y2] = c+1
    print(-1)


main()
