N = int(input())
a = list(map(int, input().split()))


a.sort()

ans = 0

for i in reversed(range(N)):
    ans += a[3*N - (i+1)*2]

print(ans)
