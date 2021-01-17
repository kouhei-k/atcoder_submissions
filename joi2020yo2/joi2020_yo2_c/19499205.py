def main():
    N = int(input())
    d = dict()
    ans = 1
    A = []
    d[N] = 1
    for i in range(N-1, 0, -1):
        x = i
        for y in str(i):
            x += int(y)
        if x > N:
            d[i] = 0
        else:
            ans += d[x]
            d[i] = d[x]

    print(ans)


main()
