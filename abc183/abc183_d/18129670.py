N, W = map(int, input().split())

A = [0]*(2*10**5 + 2)

for i in range(N):
    S, T, P = map(int, input().split())
    A[S] += P
    A[T] -= P

SA = [0]*(2*10**5 + 3)
flag = True
for i in range(2*10**5 + 2):
    SA[i+1] = SA[i] + A[i]
    if SA[i+1] > W:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
