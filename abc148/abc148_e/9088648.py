N = int(input())
l = len(str(N))
if N < 2:
    print(0)
elif N % 2 == 1:
    print(0)
else:
    ans = 0

    for i in range(2*l):
        ans += (N // (10 * (5**i)))
    print(ans)
