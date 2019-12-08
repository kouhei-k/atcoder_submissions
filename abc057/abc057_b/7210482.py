N,M = map(int,input().split())
ab = [[0,0]] * N
cd = [[0,0]] * M

distance = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    ab[i] = list(map(int, input().split()))

for i in range(M):
    cd[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        distance[i][j] = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])

for i in range(N):
    print(distance[i].index(min(distance[i])) + 1)
