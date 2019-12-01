import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = [int(input()) for i in range(N)]
diff = [0]*(N-1)
s = [0]*N


ans = 0
for i in range(N-1):
    if A[i] < A[i+1]:
        diff[i] = 1

for i in range(N-1):
    s[i+1] = s[i] + diff[i]

for i in range(N - K + 1):
    if s[i+K-1] - s[i] == K-1:
        ans += 1

print(ans)
