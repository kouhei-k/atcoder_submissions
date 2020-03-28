def main():
    import heapq
    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    hq = [None]*(A+B+C)
    for i, x in enumerate(p):
        hq[i] = (-x, 0)
    for i, x in enumerate(q):
        hq[A+i] = (-x, 1)
    for i, x in enumerate(r):
        hq[A+B+i] = (-x, 2)

    heapq.heapify(hq)

    hq2 = []

    x = 0
    y = 0
    ans = 0
    while(len(hq2) < X+Y - (x+y)):
        a, b = heapq.heappop(hq)
        a = -a
        if b == 0:
            if x < X:
                x += 1
                ans += a
            else:
                continue
        elif b == 1:
            if y < Y:
                y += 1
                ans += a
            else:
                continue
        else:
            hq2.append(a)
        if x == X and y == Y:
            break

    if x < X or y < Y:
        ans += sum(hq2)
    print(ans)


main()
