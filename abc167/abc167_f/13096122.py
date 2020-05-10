N = int(input())
s = [input() for i in range(N)]
S = [[0]*len(s[i]) for i in range(N)]
for i, x in enumerate(s):
    res = []
    q = 0
    for j in range(len(x)):
        if x[j] == ')':
            S[i][j] = -1
        else:
            S[i][j] = 1
s = [0]*N
m = [len(S[i]) for i in range(N)]
for i, x in enumerate(S):
    tmp = 0
    for j in range(len(x)):
        tmp += S[i][j]
        m[i] = min(tmp, m[i])
    s[i] = tmp

if sum(s) == 0:
    sp = [(m[i], s[i]) for i in range(N) if s[i] > 0]
    mp = [(-(s[i]-m[i]), -s[i]) for i in range(N) if s[i] <= 0]#右から見た場合
    sp.sort(key=lambda x: x[0], reverse=True)
    tmp = 0
    for x, y in sp:
        if tmp + x < 0:
            print("No")
            exit(0)
        tmp += y
    mp.sort(key=lambda x: x[0], reverse=True)
    tmp2 = 0
    for x, y in mp:
        if tmp2 + x < 0:
            print("No")
            exit(0)
        tmp2 += y
    print("Yes")

else:
    print("No")
