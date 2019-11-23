H, W, K = map(int, input().split())
s = [list(input()) for i in range(H)]

ans = [[-1]*W for i in range(H)]
pieces = [False]*H

for i in range(H):
    if "#" in s[i]:
        pieces[i] = True

count = 0
for i in range(H):
    if pieces[i] == False:
        continue
    flag = False
    count += 1

    for j in range(W):
        if s[i][j] == "#":
            if flag:
                count += 1
            else:
                flag = True

        ans[i][j] = count
count = 0
for i in range(H):
    if pieces[i] == False:
        count += 1
    else:
        for k in range(count):
            for j in range(W):
                ans[i-k-1][j] = ans[i][j]
        count = 0
count = 0
for i in reversed(range(H)):
    if pieces[i] == False:
        count += 1
    else:
        for k in range(count):
            for j in range(W):
                ans[i+k+1][j] = ans[i][j]
        break

for i in range(H):
    print(" ".join(map(str, ans[i])))
