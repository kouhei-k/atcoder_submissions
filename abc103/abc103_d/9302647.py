
N, M = map(int, input().split())

ab = [tuple(map(int, input().split())) for i in range(M)]

ab = [tuple([ab[i][0], ab[i][1], i]) for i in range(M)]
ans = 1
tmp = 0

a = sorted(ab, key=lambda x: x[0])
b = sorted(ab, key=lambda x: x[1])

checked = set()

for i in range(M):
    if b[tmp][1] <= a[i][0]:
        ans += 1
        while(b[tmp][1] <= a[i][0] or b[tmp][2] in checked):
            tmp += 1
    checked.add(a[i][2])

print(ans)
