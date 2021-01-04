def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = 0
    dp = [0]*(m+1)
    l = 0
    r = 1
    while(l < n and r <= n):
        if s[l:r] in t:
            if r-l > ans:
                ans = r-l
            r += 1
        else:
            l += 1
    print(ans)


main()
