N = int(input())
AB = [tuple(map(int, input().split())) for i in range(N)]
A = [AB[i][0] for i in range(N)]
B = [AB[i][1] for i in range(N)]

A.sort()
B.sort()
if N % 2 == 1:
    id = (N+1)//2
    print(B[-id] - A[id-1] + 1)
else:
    id = N // 2
    ans = (B[-id-1]-A[id])*2 + 1
    ans += B[-id] - B[-id-1]

    ans += A[id] - A[id-1]

    print(ans)
