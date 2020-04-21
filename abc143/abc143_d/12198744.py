import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        id = bisect.bisect_left(L, L[i] + L[j])
        ans += id - j - 1

print(ans)
