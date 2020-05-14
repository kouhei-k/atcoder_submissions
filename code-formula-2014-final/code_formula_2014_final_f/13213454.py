used = [0]*100
x = 0
y = 0
ans = [[0, 0] for i in range(100)]
P = 100
for i in range(100, 0, -1):
    if used[i-1]:
        continue
    else:
        used[i-1] = 1
        ans[i-1][0] = x+i
        ans[i-1][1] = y + i

        if i == P:
            x += 2*i
            continue
        else:
            if used[P-i-1] == 0:
                ans[P-i-1][0] = x+i
                ans[P-i-1][1] = y + i*2 + P-i
                used[P-i-1] = 1
        x += 2*i
        if x+2*(i-1) > 1500:
            x = 0
            y += 2 * P
            P = i-1
for i in range(100):
    print(*ans[i])
