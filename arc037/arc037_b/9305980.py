import collections
N, M = map(int, input().split())
G = [set() for i in range(N)]
for i in range(M):
    v1, v2 = map(int, input().split())
    G[v1-1].add(v2-1)
    G[v2-1].add(v1-1)


q = collections.deque()
reached = [0]*N
ans = 0
loop = True
k = 0
flag = False
while(loop):
    for i in range(N):
        if reached[i] == 0:
            k += 1
            reached[i] = k
            q.append((i, -1))
            flag = True
            break
        elif i == N-1:
            loop = False
            break

    while(q):
        x, g = q.popleft()

        for y in G[x]:
            if reached[y] > 0:
                if y == g:
                    continue
                elif reached[y] == k:
                    flag = False
            else:
                reached[y] = k
                q.append((y, x))
    if flag:
        ans += 1
        flag = False


print(ans)
