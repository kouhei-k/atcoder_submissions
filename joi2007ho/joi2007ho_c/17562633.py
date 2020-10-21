def main():
    import sys
    input = sys.stdin.buffer.readline
    n = int(input())
    xy = [tuple(map(int, input().split())) for i in range(n)]

    s = set(xy)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            X = xy[j][0] - xy[i][0]
            Y = xy[j][1] - xy[i][1]
            if (xy[i][0]-Y, xy[i][1]+X) in s and (xy[j][0]-Y, xy[j][1]+X) in s:
                S = (abs(X)+abs(Y))**2 - (abs(X)*abs(Y))*2
                if S > ans:
                    ans = S

    print(ans)


main()
