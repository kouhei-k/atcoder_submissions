N = int(input())
A = list(map(int, input().split()))

sa = [0]*(N+1)
for i in range(N):
    sa[i+1] = sa[i] + A[i]
    if i > 0:
        sa[i+1] += 1

ssa = [0] * (N+1)
for i in range(N):
    ssa[i+1] = ssa[i] + sa[i+1]

ra = [0]*(N+1)
for i in range(N):
    ra[i+1] = ra[i] + A[N-1-i]
    if i > 0:
        ra[i+1] += 1

rra = [0]*(N+1)
for i in range(N):
    rra[i+1] = rra[i] + ra[i+1]

ans = float("Inf")
for i in range(0, N, 2):
    tmp = ssa[i] + rra[N-i-1]
    ans = min(ans, tmp)

# print(ssa, rra)
print(ans)
