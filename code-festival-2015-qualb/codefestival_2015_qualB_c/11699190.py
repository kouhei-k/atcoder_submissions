N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if N < M:
    print("NO")
else:
    A.sort()
    B.sort()
    for i in range(M):
        x = A.pop()
        y = B.pop()
        if x >= y:
            continue
        else:
            print("NO")
            exit(0)
    print("YES")
