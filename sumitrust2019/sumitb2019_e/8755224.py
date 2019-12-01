N = int(input())
A = list(map(int, input().split()))

countA = [0]*(max(A)+1)
ans = 1
mod = 10**9 + 7
for i in range(N):
    if A[i] == 0:
        ans *= (3 - countA[A[i]])
    else:
        ans *= (countA[A[i]-1] - countA[A[i]])
    countA[A[i]] += 1
    ans %= mod
print(max(ans, 0))
