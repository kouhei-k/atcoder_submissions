N, T = map(int, input().split())

AB = [tuple(map(int, input().split())) for i in range(N)]
sa = 0
sb = 0
for i in range(N):
    sa += AB[i][0]
    sb += AB[i][1]
if sb > T:
    print(-1)
    exit(0)
elif sa <= T:
    print(0)
    exit(0)
else:
    AB.sort(key=lambda x: x[0] - x[1])
    t = sa
    ans = 0
    for i in range(N-1, -1, -1):
        ans += 1
        t -= (AB[i][0] - AB[i][1])
        if t <= T:
            break

    print(ans)
