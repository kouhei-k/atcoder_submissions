N = int(input())
A = [0]*N
ans = 0
tmp = 0
for i in range(N):
    A[i] = int(input())
    ans += (A[i] + tmp) // 2
    if A[i] != 0:
        tmp = (A[i]+tmp) % 2
    else:
        tmp = 0


print(ans)
