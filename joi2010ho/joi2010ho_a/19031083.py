n, m = map(int, input().split())
s = [int(input()) for i in range(n-1)]

ss = [0]*n

for i in range(1, n):
    ss[i] = ss[i-1] + s[i-1]

prev = 0
ans = 0
for i in range(m):
    next = int(input())
    ans += abs(ss[prev+next] - ss[prev])
    prev += next
print(ans % (10**5))
