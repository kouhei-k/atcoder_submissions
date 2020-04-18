N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(N)]
AB.sort()

ans = 0
for a, b in AB:
    if M > b:
        M -= b
        ans += a*b
    else:
        ans += a*M
        break

print(ans)
