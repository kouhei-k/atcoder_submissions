def main():
    A, B, X = map(int, input().split())

    l = 0
    r = 10**9 + 1
    while(l + 1 < r):
        mid = (l + r) // 2
        if X >= A*mid + B * len(str(mid)):
            l = mid
        else:
            r = mid
    print(l)


main()
