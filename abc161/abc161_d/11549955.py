N = int(input())
tmp = [i for i in range(1, 10)]
ans = list(tmp)
for i in range(10):
    tmp2 = []
    for x in tmp:
        k = int(str(x)[-1])
        if k != 0:
            ans.append(10*x-1 + k)
            tmp2.append(10*x-1 + k)
        if k != 9:
            tmp2.append(10*x+1 + k)
            ans.append(10*x+1 + k)
        tmp2.append(10*x + k)
        ans.append(10*x + k)
    tmp = list(tmp2)

ans.sort()
print(ans[N-1])
