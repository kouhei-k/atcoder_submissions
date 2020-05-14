import collections
N = int(input())
A = list(map(int, input().split()))
B = [A[i] - (i+1) for i in range(N)]

B.sort()

ans = 0
t = B[len(B)//2]

for x in B:
    ans += abs(x - t)

print(ans)
