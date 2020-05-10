import collections
first, last = input().split()
N = int(input())
s = [input() for i in range(N)]

d = [-1]*N


def check(s1, s2):
    n = len(s1)
    count = 0
    for i in range(n):
        if s1[i] == s2[i]:
            continue
        else:
            count += 1
        if count > 1:
            return(False)
    return(True)


G = [set() for i in range(N+2)]

if check(first, last):
    G[0].add(N+1)
for i in range(N):
    if check(first, s[i]):
        G[0].add(i+1)
    for j in range(i, N):
        if check(s[i], s[j]):
            G[i+1].add(j+1)
            G[j+1].add(i+1)

    if check(s[i], last):
        G[i+1].add(N+1)

q = collections.deque()
q.append(0)

r = [True]*(N+2)
r[0] = False
prev = [0]*(N+2)
while(q):
    x = q.popleft()
    for y in G[x]:
        if r[y]:
            q.append(y)
            prev[y] = x
            r[y] = False
if r[N+1]:
    print(-1)
else:
    ans = []
    crr = N+1

    while(crr != 0):
        crr = prev[crr]
        if crr == 0:
            break
        ans.append(s[crr-1])
    print(len(ans))
    print(first)
    if ans:
        print(*ans[::-1], sep='
')
    print(last)
