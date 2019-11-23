import bisect
N = int(input())
A = list(map(int, input().split()))

s = [0]*N
s[0] = A[0]
for i in range(1, N):
    s[i] = s[i-1] + A[i]

id = bisect.bisect_left(s, s[-1] // 2)
if s[id] == s[-1] // 2:
    if s[-1] % 2 == 0:
        print(0)
    else:
        print(1)
else:
    k = 0
    if s[-1] % 2 != 0:
        k = 1
    ans = abs(s[id]*2 - s[-1])
    if id > 0:
        ans = min(ans, abs(s[id-1]*2 - s[-1]))
    print(ans)
