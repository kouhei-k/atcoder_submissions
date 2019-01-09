N,M,K = map(int, input().split())
field = [[0]*M for i in range(N)]
def reverse(x):
    if x == 0:
        return 1
    else:
        return 0
now = 0
for i in range(N+1):
    if N - 2 * i ==0:
        for j in range(M):
           now += M
    elif (K - now) % (N - 2 * i) == 0 and (K - now) / (N - 2 * i) <= M and  (K - now) / (N - 2 * i) >= 0:
        print("Yes")
        exit(0)
    elif i == N:
        print("No")
        exit(0)
    else:
        now += M
