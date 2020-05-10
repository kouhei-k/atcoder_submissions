N, K = map(int, input().split())
A = list(map(int, input().split()))
order = [-1]*N
crr = 0
T = 0
s = -1
order[0] = 0
for i in range(N+1):
    crr = A[crr] - 1
    if order[crr] >= 0:
        T = (i+1) - order[crr]
        s = order[crr]
        break
    order[crr] = i+1

if K <= s:
    crr = 0
    while(K):
        K -= 1
        crr = A[crr]-1
    print(crr+1)
else:
    k = K-s
    d = k % T
    while(d):
        d -= 1
        crr = A[crr]-1
    print(crr+1)
