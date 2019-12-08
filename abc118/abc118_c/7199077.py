import copy
N = int(input())
A = list(map(int,input().split()))

A = sorted(A)

ans = min(A)
while(1):
    prev = ans
    B = list(map(lambda x: x % ans , A[1:]))
    A = [ans] + [i for i in B if i != 0]
    ans = min(A)
    if ans == prev:
        print(ans)
        exit(0)
    A = sorted(A)
