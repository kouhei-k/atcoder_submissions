N = int(input())
S = list(map(int, input().split()))
A = []
prev = -1
c = 0
for x in S:
    if x != prev:
        c += 1
    else:
        A.append(c)
        c = 1
    prev = x
A.append(c)
if len(A) == 1:
    print(N)
else:
    ans = max(A[0] + A[1], A[-1] + A[-2])
    for i in range(1, len(A)-1):
        ans = max(ans, A[i] + A[i-1] + A[i+1])
    print(ans)
