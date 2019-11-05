import collections
N, M = map(int, input().split())
x = [[0, 0] for i in range(N)]
y = [[0, 0] for i in range(N)]
z = [[0, 0] for i in range(N)]
xyz = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    x[i][0], y[i][0], z[i][0] = xyz[i][0], xyz[i][1], xyz[i][2]
    x[i][1], y[i][1], z[i][1] = i, i, i

ans = 0
for k in range(2**3):
    flag = [1, 1, 1]
    tmp = [0, 0, 0]
    for l in range(3):
        if (k >> l) % 2 == 1:
            flag[l] = -1
        else:
            flag[l] = 1
    # print(flag)
    xyz.sort(reverse=True, key=lambda x: x[0]
             * flag[0] + x[1]*flag[1] + x[2]*flag[2])

    for i in range(M):
        tmp[0] += xyz[i][0]
        tmp[1] += xyz[i][1]
        tmp[2] += xyz[i][2]
    # print(abs(tmp[0]) + abs(tmp[1]) + abs(tmp[2]))
    # print(xyz)
    ans = max(ans, abs(tmp[0]) + abs(tmp[1]) + abs(tmp[2]))
print(ans)
