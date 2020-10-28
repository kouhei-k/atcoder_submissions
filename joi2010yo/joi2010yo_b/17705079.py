N, M = map(int, input().split())
p = 0
X = [int(input()) for i in range(N)]
for i in range(M):
    p += int(input())
    if p >= N-1:
        print(i + 1)
        exit(0)
    else:
        p += X[p]
        if p >= N-1:
            print(i+1)
            exit(0)
