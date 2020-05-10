import collections
N, K = map(int, input().split())
t = [int(input()) for i in range(N)]


q = collections.deque()
ans = -1
for i, x in enumerate(t):
    if len(q) == 3:
        q.popleft()
    q.append(x)
    if len(q) == 3 and sum(q) < K:
        ans = i+1
        break
print(ans)
