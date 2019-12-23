s = list(input().split("T"))
x, y = map(int, input().split())
s2 = [len(x) for x in s]
LR = [s2[i] for i in range(len(s2)) if i % 2 == 0]
UD = [s2[i] for i in range(len(s2)) if i % 2 == 1]

flag = False
tmp = 1
tmp = tmp << sum(LR)
for i, d in enumerate(LR):
    if i != 0:
        tmp = tmp << d | tmp >> d
    else:
        tmp = tmp << d

if x >= 0:
    tmp = tmp >> sum(LR)
    if (tmp >> x) % 2 == 1:
        flag = True
else:
    if sum(LR) + x >= 0:
        if (tmp >> (sum(LR) + x)) % 2 == 1:
            flag = True
if flag:

    tmp = 1
    tmp = tmp << sum(UD)
    flag = False
    for d in UD:
        tmp = tmp << d | tmp >> d
    if y >= 0:
        tmp = tmp >> sum(UD)
        if (tmp >> y) % 2 == 1:
            flag = True
    else:
        if sum(UD) + y >= 0:
            if (tmp >> (sum(UD) + y)) % 2 == 1:
                flag = True

if flag:
    print("Yes")
else:
    print("No")
