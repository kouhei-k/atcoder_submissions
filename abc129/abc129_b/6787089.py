N = int(input())
W = list(map(int,input().split()))
S = [0] * N
S[0] = W[0]
sumW = sum(W)
for i in range(1,N):
  S[i] = S[i - 1] + W[i]
ans = max(W)
for i in range(N):
  ans = min(ans, abs(sumW - 2 * S[i]))
print(ans)
