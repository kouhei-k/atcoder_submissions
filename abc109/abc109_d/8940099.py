H, W = map(int, input().split())
a = [list(map(int, input().split())) for i in range(H)]
flag = False
prev = [-1, -1]
ans = []
for i in range(0, H, 2):
    for j in range(W):
        if flag:
            ans.append(" ".join(map(str, [prev[0], prev[1], i+1, j+1])))
            a[i][j] += 1
            flag = False
        if a[i][j] % 2 == 1:
            flag = True
            prev = [i+1, j+1]
    if i < H-1:
        for j in reversed(range(W)):
            if flag:
                ans.append(" ".join(map(str, [prev[0], prev[1], i+2, j+1])))
                a[i+1][j] += 1
                flag = False
            if a[i+1][j] % 2 == 1:
                flag = True
                a[i+1][j] -= 1
                prev = [i+2, j+1]

print(len(ans))
for x in ans:
    print(x)
