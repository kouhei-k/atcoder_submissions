N = tuple(input())
N = tuple(map(int, N))


ans = 0
flag = False
flag5 = False
for i in range(len(N)-1, -1, -1):
    x = N[i]
    if flag or (flag5 and x >= 5):
        x += 1
    flag5 = False
    flag = False
    if x > 5:
        ans += (10 - x)
        flag = True
        if i == 0:
            ans += 1
    else:
        ans += x
    if x == 5:
        flag5 = True
print(ans)
