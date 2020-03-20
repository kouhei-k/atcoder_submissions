
def main():
    import math
    N, A, B = map(int, input().split())
    h = [int(input()) for i in range(N)]
    d = A - B

    l = 1
    r = max(h)
    while(l+1 < r):
        m = (l+r)//2
        t = m*B
        count = 0
        for x in h:
            if x > t:
                count += math.ceil((x-t)/d)
        if count <= m:
            r = m
        else:
            l = m

    print(r)


main()
