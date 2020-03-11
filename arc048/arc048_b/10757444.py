def main():
    import sys
    import bisect
    import collections
    input = sys.stdin.readline
    N = int(input())
    RH = [tuple(map(int, input().split())) for i in range(N)]
    table = collections.defaultdict(list)
    for r, h in RH:
        if r not in table:
            table[r] = [0, 0, 0]
        table[r][h-1] += 1

    R = [RH[i][0] for i in range(N)]
    R.sort()

    ans = [[0]*3 for i in range(N)]
    for i, x in enumerate(RH):
        r, h = x
        ans[i][0] = bisect.bisect_left(R, r)
        ans[i][1] = N - bisect.bisect_right(R, r)

        h -= 1
        table[r][h] -= 1
        ans[i][0-h] += table[r][1]
        ans[i][1-h] += table[r][2]
        ans[i][2-h] += table[r][0]
        table[r][h] += 1
        print(*ans[i])


main()
