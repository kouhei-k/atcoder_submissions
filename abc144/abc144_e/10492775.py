import heapq
N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
S = sum(A)
if S <= K:
    print(0)

else:
    A.sort()
    F.sort(reverse=True)

    r = A[-1]*F[0]

    l = 0

    while(1):
        tmp = (l+r)//2
        k = 0
        for x, y in zip(A, F):
            k += max(0, x - (tmp // y))
        if k > K:
            l = tmp
        else:
            r = tmp

        if l+1 == r:
            print(r)
            exit(0)
