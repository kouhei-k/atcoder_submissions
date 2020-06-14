
def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    A = list(map(int, input().split()))

    d = dict()
    for x in A:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    A.sort()

    ans = 0
    M = max(A)
    dp = [True]*(M+1)
    for x in A:
        for xx in range(x+x, M+1, x):
            dp[xx] = False
    for x in A:
        if d[x] == 1 and dp[x]:
            ans += 1
    print(ans)


main()
