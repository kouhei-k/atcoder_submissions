a, b = map(int, input().split())
n = int(input())
G = set()
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G.add((x, y))
ans = [[0]*b for i in range(a)]
ans[0][0] = 1
for i in range(a):
    for j in range(b):
        if i < a-1 and (i+1, j) not in G:
            ans[i+1][j] += ans[i][j]
        if j < b-1 and (i, j+1) not in G:
            ans[i][j+1] += ans[i][j]
print(ans[-1][-1])
