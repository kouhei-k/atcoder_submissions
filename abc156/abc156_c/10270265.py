N = int(input())
X = list(map(int, input().split()))

ans = 10**9

for P in range(1, 100):
    tmp = 0
    for x in X:
        tmp += (x-P)**2

    ans = min(ans, tmp)
print(ans)
