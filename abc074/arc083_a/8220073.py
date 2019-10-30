A, B, C, D, E, F = map(int, input().split())

water = set()
for i in range(F//(100*A) + 1):
    for j in range(F // (100*B) + 1):
        if 100*A * i + 100*j*B <= F:
            water |= {100*A * i + 100*j*B}
        else:
            break

sugar = set()
for i in range(F//C + 1):
    for j in range(F // D + 1):
        if C * i + D*j <= F:
            sugar |= {C * i + D*j}
        else:
            break
ans = [100*A, 0]
for x in water:
    if x == 0:
        continue
    for y in sugar:
        if x + y <= F and y <= (x/100)*E:
            if ans[1]/ans[0] < y / (x+y):
                ans = [x+y, y]

print(ans[0], ans[1])
