import collections
N, K = map(int, input().split())
s = [int(input()) for i in range(N)]
if min(s) == 0:
    print(N)
    exit(0)
q = collections.deque()
ans = 0
product = 1
for i in range(N):
    while(q and product * s[i] > K):
        x = q.popleft()
        product //= x

    if s[i] <= K:
        q.append(s[i])
        product *= s[i]
    ans = max(ans, len(q))


print(ans)
