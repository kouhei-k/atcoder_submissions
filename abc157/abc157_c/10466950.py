import collections
N, M = map(int, input().split())
sc = [tuple(map(int, input().split())) for i in range(M)]
t = collections.defaultdict(int)
flag = True
for s, c in sc:
    if s in t and t[s] != c:
        flag = False
        break
    else:
        t[s] = c

if flag:
    ans = []
    for i in range(1, N+1):
        if i in t:
            if i == 1 and t[i] == 0 and N > 1:
                print(-1)
                exit(0)
            else:
                ans.append(t[i])
        else:
            if i != 1:
                ans.append(0)
            else:
                if N == 1:
                    ans.append(0)
                else:
                    ans.append(1)

    print("".join(map(str, ans)))
else:
    print(-1)
