N = int(input())
l = len(str(N))
if N < 2:
    print(0)
elif N % 2 == 1:
    print(0)
else:
    ans = 0

    for i in range(1, 2*l):
        tmp = 0
        ans += (N // 10**i)
        tmp += (N // (10 * (5**i)))
        tmp -= N // (10 * (10**i))
        ans += max(tmp, 0)

    print(ans)
