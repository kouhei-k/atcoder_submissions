import collections
N = int(input())
p = list(map(int, input().split()))

q = collections.deque([i for i in range(N+1)])
s = set()
for x in p:
    s.add(x)
    while(q[0] in s):
        q.popleft()
    print(q[0])
