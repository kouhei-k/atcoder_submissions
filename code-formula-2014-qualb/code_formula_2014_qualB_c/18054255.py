import sys
A = input()
B = input()
sys.setrecursionlimit(10**5)
a = []
b = []
f = False
d = dict()
d2 = dict()
for x, y in zip(A, B):
    if x != y:
        a.append(x)
        b.append(y)
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
    if y in d2:
        d2[y] += 1
    else:
        d2[y] = 1

    if d[x] >= 2:
        f = True

for x in d:
    if x in d2:
        if d[x] == d2[x]:
            continue
        else:
            print("NO")
            exit(0)
    else:
        print("NO")
        exit(0)

r = len(A) - len(a)

if len(a) > 6:
    print("NO")
    exit(0)

# if len(a) == 0:
#     if r >= 3 or f:
#         print("YES")
#         exit(0)
#     else:
#         print("NO")
#         exit(0)


def solve(a, b, n, r, f):
    if "".join(a) == "".join(b):
        if n == 3 or n == 1 or f:
            return(True)
        else:
            return(False)
    elif n == 3:
        return(False)
    else:
        for i in range(len(a)-1):
            for j in range(i+1, len(a)):
                c = a[:]
                c[i], c[j] = a[j], a[i]
                if solve(c, b, n+1, r, f):
                    return(True)
        return(False)


if solve(a, b, 0, r, f):
    print("YES")
else:
    print("NO")
