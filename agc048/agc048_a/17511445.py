import collections
T = int(input())

for _ in range(T):
    S = input()
    flag = True
    ans = 10**3
    s = list(S)
    s = "".join(sorted(s, reverse=True))
    if s < 'atcoder':
        print(-1)
        continue
    A = 'atcoder'
    K = min(7, len(S))
    f = 0
    if A < S:
        print(0)
        continue
    N = len(S)

    if S[1] >= 'b':
        print(1)
        continue
    else:
        tmp = 0
        D = collections.defaultdict(collections.deque)
        for i, x in enumerate(S):
            D[x].append(i)
        # U = [0]*N

        # d = dict()
        # for i, x in enumerate('abcdefghijklmnopqrstuvwxyz'):
        #     d[x] = i
        # alpha = 'abcdefghijklmnopqrstuvwxyz'
        prev = 0
        for i in range(7):
            tmp = 10**5
            for y in D:
                if y <= A[i]:
                    continue
                else:
                    if len(D[y]) > 0:
                        tmp = min(tmp, D[y][0])
            ans = min(ans, tmp - i + prev)
            if len(D[A[i]]) > 0:
                p = D[A[i]].popleft()
                prev += p - i
                for x in D:
                    # print(D[x])
                    for j in range(len(D[x])):
                        if i <= D[x][j] < p:
                            D[x][j] += 1
            else:
                break

        print(ans)
