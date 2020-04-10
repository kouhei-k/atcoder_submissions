import collections
N = int(input())
G = [set() for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)


F = [-1]*N
F[0] = 0
q = collections.deque()
q.append(0)
while(q):
    x = q.popleft()
    for y in G[x]:
        if F[y] < 0:
            F[y] = F[x] + 1
            q.append(y)

S = [-1]*N
S[N-1] = 0
q.append(N-1)
while(q):
    x = q.popleft()
    for y in G[x]:
        if S[y] < 0:
            S[y] = S[x] + 1
            q.append(y)
# print(F)
# print(S)
ans = 0

q = collections.deque()
r = [True]*N
for i in range(N):
    if F[i] + S[i] == F[-1]:
        if F[i] <= S[i]:
            q.append(i)
            r[i] = False
        else:
            r[i] = False
ans = len(q)

while(q):
    x = q.popleft()
    for y in G[x]:
        if r[y]:
            ans += 1
            q.append(y)
            r[y] = False

if ans > N - ans:
    print("Fennec")
else:
    print("Snuke")
