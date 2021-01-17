N, M = map(int, input().split())
P = list(map(int, input().split()))
ABC = [tuple(map(int, input().split())) for i in range(N-1)]


S = [0]*N
for a, b in zip(P, P[1:]):
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    S[a] += 1
    S[b] -= 1

SS = [0]*N
ans = 0
for i in range(N-1):
    SS[i] = SS[i-1] + S[i]
    a, b, c = ABC[i]
    if (a-b)*SS[i] > c:
        ans += b*SS[i] + c
    else:
        ans += a*SS[i]
print(ans)
