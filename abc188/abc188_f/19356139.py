def main():
    import sys
    sys.setrecursionlimit(10**5)
    import bisect
    X, Y = map(int, input().split())

    d = dict()

    if X != 1:
        d[1] = Y - 1

    if X >= Y:
        print(X-Y)
        exit(0)
    ans = 0

    d[X] = 0

    def solve(x):
        ret = 0
        if x in d:
            return(d[x])
        if x % 2 == 1:
            ret += min(abs(X-x), solve((x-1)//2) +
                       2, solve((x+1)//2)+2)
        else:
            ret += min(abs(X-x), solve(x // 2)+1)
        d[x] = ret
        return(ret)

    print(solve(Y))


main()
