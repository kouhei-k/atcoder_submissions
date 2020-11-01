S = input()

s = set(S)
d = dict()

for x in S:
    if x in d:
        d[x] += 1

    else:
        d[x] = 1

if len(S) == 1:
    if S == '8':
        print("Yes")
    else:
        print("No")
elif len(S) == 2:
    for i in range(2, 13):
        x = 8*i
        x = str(x)
        if i == 11:
            if '8' in d and d['8'] == 2:
                print("Yes")
                exit(0)
        else:
            if x[0] in d and x[1] in d:
                print("Yes")
                exit(0)
    print("No")
else:
    num = '0123456789'
    for i in range(13, 125):
        x = 8 * i
        x = str(x)
        c = [0]*10
        for y in x:
            c[num.index(y)] += 1
        flag = True
        for y in x:
            if y in d and c[num.index(y)] <= d[y]:
                continue
            else:
                flag = False
                break

        if flag:
            print("Yes")
            exit(0)

    print("No")
