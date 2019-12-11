N = int(input())

k = N*2
flag = False
tmp = 0
if N == 1:
    print("Yes")
    print(2)
    print(1, 1)
    print(1, 1)
    exit(0)
for x in range(2, int(k ** 0.5) + 1):
    if k % x == 0 and k // x == x+1:
        tmp = x
        flag = True
        break
if flag:
    print("Yes")
    print(tmp+1)
    ans = [[] for i in range(tmp+1)]
    count = 0
    for i in range(tmp+1):
        ret = [str(tmp)]
        for k in range(i):
            ret.append(ans[k][i])
        for j in range(tmp):
            if i == 0:
                count += 1
                ret.append(str(count))
            else:
                if j < tmp - i:
                    count += 1
                    ret.append(str(count))

        ans[i] = ret
    for i in range(tmp+1):
        print(" ".join(ans[i]))
else:
    print("No")
