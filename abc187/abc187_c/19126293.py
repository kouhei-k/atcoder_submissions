N = int(input())
S = [input() for i in range(N)]
S.sort(reverse=True)
flag = True
ans = None
d = dict()
for x in S:
    k = None
    if x[0] == '!':
        k = x[1:]
        if k in d:
            flag = False
            ans = k
            break
    else:
        d[x] = 1

if flag:
    print("satisfiable")
else:
    print(ans)
