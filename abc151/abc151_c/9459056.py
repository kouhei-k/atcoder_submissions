N, M = map(int, input().split())
pS = [tuple(input().split()) for i in range(M)]
pS.sort(key=lambda x: x[0])
problems = [0]*N
AC = 0
penalty = 0

for p, S in pS:
    p = int(p)
    if problems[p-1] < 0:
        continue
    else:
        if S == "AC":
            penalty += problems[p-1]
            problems[p-1] = -1
            AC += 1

        else:
            problems[p-1] += 1

print(AC, penalty)
