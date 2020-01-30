import sys
import bisect
import math
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

B = [(A[i]*F[i], F[i]) for i in range(N)]
B.sort(reverse=True)
L = 0
R = B[0][0]
if sum(A) <= K:
    print(0)
    exit(0)
while(1):
    ans = (L+R) // 2
    flag = True
    tmp = 0
    for i in range(N):
        tmp += math.ceil(max(B[i][0] - ans, 0) / B[i][1])
        if tmp > K:
            flag = False
            break
    if flag:
        R = ans
    else:
        L = ans
    if L == R or L+1 == R:
        print(R)
        break
