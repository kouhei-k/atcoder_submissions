import math
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
prev = 0
c = 0
B = []
for i in range(M):
    c = A[i] - prev - 1
    if c > 0:
        B.append(c)
    prev = A[i]
c = N - prev
if c > 0:
    B.append(c)
if B:
    k = min(B)

    ans = 0

    for x in B:
        ans += math.ceil(x / k)
    print(ans)
else:
    if M == 0:
        print(1)
    else:
        print(0)
