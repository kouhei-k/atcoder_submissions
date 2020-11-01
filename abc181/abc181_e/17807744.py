import bisect
N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()


D = [H[i] - H[i-1] for i in range(1, N)]

SE = [0]*(((N+1) // 2))
SO = [0]*(((N+1) // 2))

for i in range((N+1) // 2 - 1):
    SE[i+1] = SE[i] + D[i*2]
    SO[i+1] = SO[i] + D[i*2 + 1]
# print(SE)
# print(SO)
ans = 10**15

idx = 0

for i in range(M):
    tmp = 0
    id = bisect.bisect_left(H, W[i])
    if id == 0:
        tmp = SO[-1] + H[0] - W[i]
    elif id == 1:
        tmp = SO[-1] - H[0] + W[i]
    elif id == N:
        tmp = SE[-1] + W[i] - H[-1]
    elif id == N-1:
        tmp = SE[-1] - W[i] + H[-1]
    else:
        # print(id, id // 2)
        if id % 2 == 0:
            tmp = SE[id // 2] + (SO[-1] - SO[id // 2]) + H[id] - W[i]
        else:
            tmp = SE[id // 2] + (SO[-1] - SO[id // 2]) - H[id-1] + W[i]
    if tmp < ans:
        ans = tmp
        idx = i
# print(H)
print(ans)
# print(W[idx])
