N = int(input())
T = list(map(int, input().split()))
M = int(input())
px = [list(map(int, input().split())) for i in range(M)]

for i in range(M):
    id = px[i][0]-1
    if id >= 1:
        print(sum(T[:id]) + sum(T[id+1:]) + px[i][1])
    else:
        print(sum(T[id+1:])+px[i][1])
