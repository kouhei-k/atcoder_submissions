N = int(input())
B = []
W = []
flag = True
count = 0
for i in range(N):
    x = int(input())
    if i % 2 == 0:
        if x == 0:
            if flag == False or len(W) == 0:
                W.append(1)
            else:
                W[-1] += 1
            flag = True
        else:
            if flag or len(B) == 0:
                B.append(1)
            else:
                B[-1] += 1
            flag = False
    else:
        if x == 0:
            if flag:
                if len(W) > 0:
                    W[-1] += 1
                else:
                    W.append(1)
            else:
                y = 0
                if len(B) > 0:
                    y = B.pop()
                if len(W) > 0:
                    W[-1] += y+1
                else:
                    W.append(y+1)
            flag = True
        else:
            if flag:
                y = 0
                if len(W) > 0:
                    y = W.pop()
                if len(B) > 0:
                    B[-1] += y+1
                else:
                    B.append(y+1)
            else:
                if len(B) > 0:
                    B[-1] += 1
                else:
                    B.append(1)
            flag = False
    # print(B, W, flag)

ans = 0
for x in W:
    ans += x
print(ans)
