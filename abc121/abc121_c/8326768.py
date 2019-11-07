N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

AB.sort(key=lambda x: x[0])
ans = 0
for i in range(N):
    if M >= AB[i][1]:
        ans += AB[i][0] * AB[i][1]
        M -= AB[i][1]
    else:
        ans += AB[i][0] * M
        M = 0
    if M == 0:
        break
print(ans)
