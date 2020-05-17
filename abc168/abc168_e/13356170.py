def main():
    import math
    import collections
    N = int(input())

    mod = 10**9+7
    AB = [tuple(map(int, input().split())) for i in range(N)]

    d = collections.defaultdict(set)
    i = 0
    ans2 = 0
    for a, b in AB:
        if a == 0 and b == 0:
            N -= 1
            ans2 += 1
            continue
        g = math.gcd(a, b)
        if g != 0:
            a = a // g
            b = b // g

        d[(a, b)].add(i)
        i += 1

    ans = 0
    r = set()

    dd = [1]
    for i in range(1, N+1):
        dd.append(dd[i-1]*2 % mod)

    r = set()
    ans = 1
    for a, b in d:
        if (a, b) in r:
            continue
        s1 = d[(a, b)]
        if (-a, -b) in d:
            s1 |= d[(-a, -b)]
        l1 = len(s1)
        r.add((-a, -b))
        if l1:
            s2 = set()
            if (-b, a) in d:
                s2 |= d[(-b, a)]
            if (b, -a) in d:
                s2 |= d[(b, -a)]
            s2 -= s1
            l2 = len(s2)
            if l2:
                ans *= dd[l1] + dd[l2] - 1
                N -= l1 + l2
                ans %= mod
                r.add((-b, a))
                r.add((b, -a))
            else:
                continue
    if N:
        ans *= dd[N]
    ans += ans2
    ans -= 1
    print(ans % mod)


main()
