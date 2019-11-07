N = int(input())
h = list(map(int, input().split()))

s = [0]*(N+2)
s[1] = h[0]
s[N+1] = -h[N-1]
for i in range(1, N):
    s[i+1] = h[i] - h[i-1]
ans = 0
for x in s:
    if x > 0:
        ans += x
print(ans)
