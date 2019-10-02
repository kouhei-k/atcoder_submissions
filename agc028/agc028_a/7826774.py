import collections
import fractions
N, M = map(int, input().split())
S = input()
T = input()
lcm = (N*M) // fractions.gcd(N, M)
if S[0] != T[0]:
    print(-1)
elif N == M and S != T:
    print(-1)
else:
    tmp = lcm // N
    tmp2 = lcm // M
    tmp_s = collections.defaultdict(str)
    for i in range(N):
        tmp_s[tmp*i] = S[i]

    for i in range(M):
        if tmp2*i in tmp_s:
            if T[i] != tmp_s[tmp2*i]:
                print(-1)
                exit(0)
    print(lcm)
