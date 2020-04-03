def main():
    from itertools import combinations
    import bisect
    N, K = map(int, input().split())
    xy = [tuple(map(int, input().split())) for i in range(N)]
    xy.sort(key=lambda x: x[0])
    X = [x[0] for x in xy]

    ans = 40**18
    for a, b in combinations(range(N), 2):
        A, B = max(xy[a][0], xy[b][0]), min(xy[a][0], xy[b][0])
        r = bisect.bisect_right(X, A)
        l = bisect.bisect_left(X, B)
        for c, d in combinations(range(N), 2):
            tmp = 0
            C, D = max(xy[c][1], xy[d][1]), min(xy[c][1], xy[d][1])

            for i in range(l, r):
                if xy[i][1] <= C and xy[i][1] >= D:
                    tmp += 1
            #     print(xy[i][1], C, D)

            if tmp >= K and ans > (A-B) * (C - D):
                ans = (A-B) * (C - D)

    print(ans)
main()
