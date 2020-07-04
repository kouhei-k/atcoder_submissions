N = int(input())
s1 = input()
s2 = input()

d = dict()
ans = 1

S = []


def convert(x):
    try:
        a = int(x)
        return(x)
    except:
        for s in S:
            if x in s:
                return(s[0])
        return(x)


def addList(x, y):

    for s in S:
        if x in s:
            s.append(y)
            return
        elif y in s:
            s.append(x)
            return
    S.append([x, y])


for i in range(0, 10):
    d[str(i)] = str(i)

for i, X in enumerate(zip(s1, s2)):
    a, b = X
    a = convert(a)
    b = convert(b)
    # print(a, b)
    try:
        a = int(a)
        try:
            b = int(b)
            continue
        except:
            d[b] = a
    except:
        try:
            b = int(b)
            d[a] = b
        except:
            if a in d:
                d[b] = d[a]
            elif b in d:
                d[a] = d[b]
            else:
                addList(a, b)

# print(d)
for i, x in enumerate(s1):
    x = convert(x)
    # print(x)
    if x in d:
        continue
    else:
        if i == 0:
            ans *= 9
        else:
            ans *= 10
        d[x] = -1

print(ans)
