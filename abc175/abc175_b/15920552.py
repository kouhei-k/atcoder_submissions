import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
count = 0
for i in range(N):
    for j in range(i+1, N):
        if L[i] == L[j]:
            continue
        count += 1
        if j < N-1 and L[j] == L[j+1]:
            continue

        l = L[i] + L[j]

        id = bisect.bisect_left(L, l)
        # print(L[i], L[j], id)
        ans += (id - j - 1)*count
        count = 0
# print(L)
print(ans)
