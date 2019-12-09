N = int(input())
ab = [[0, 0] for i in range(N)]
b = [0]*N
cd = [[0, 0] for i in range(N)]
d = [0]*N

for i in range(N):
    ab[i] = list(map(int, input().split()))
for i in range(N):
    cd[i] = list(map(int, input().split()))

points = [[] for i in range(N)]
points2 = [[] for i in range(N)]
cd.sort(key=lambda x: x[0])
ab.sort(key=lambda x: x[1], reverse=True)

points.sort(key=lambda x: len(x))
ans = 0

for i in range(N):
    for j in range(N):
        if ab[i][0] < cd[j][0] and ab[i][1] < cd[j][1]:
            ans += 1
            cd[j][0] = -1
            break
print(ans)
