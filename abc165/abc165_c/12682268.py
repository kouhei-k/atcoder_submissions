from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
abcd = [tuple(map(int, input().split())) for i in range(Q)]
ans = 0
for x in combinations_with_replacement(range(1, M+1), 10):
    tmp = 0

    for a, b, c, d in abcd:
        a -= 1
        b -= 1
        if x[a] + c == x[b]:
            tmp += d
    ans = max(ans, tmp)


print(ans)
