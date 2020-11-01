N = int(input())
xy = [tuple(map(int, input().split())) for i in range(N)]
xy.sort()
s = set()
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            X = xy[j][0] - xy[i][0]
            Y = xy[j][1] - xy[i][1]
            X2 = xy[k][0] - xy[i][0]
            Y2 = xy[k][1] - xy[i][1]

            if X*Y2 == X2 * Y:
                print("Yes")
                exit(0)
print("No")
