import collections
N = int(input())
A = list(map(int, input().split()))

s = set()
ans = 0

flag = True
q = collections.deque()
for x in A:

    if x in s:
        count = 0
        while(q):
            y = q.popleft()
            s.remove(y)
            if y == x:
                break
    q.append(x)
    s.add(x)
    if len(q) > ans:
        ans = len(q)

ans = max(ans, len(q))
print(ans)
