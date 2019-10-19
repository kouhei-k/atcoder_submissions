import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
R = sorted(L)
ans = 0
diff = [L[i] - L[i+1] for i in range(N-1)]

for i in range(N):
    d = 0
    for j in range(i+1, N):
        d += diff[j-1]
        k = bisect.bisect_left(R, d+1)
        ans += max(N-k-1 - j, 0)

print(ans)
