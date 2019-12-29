import sys
input = sys.stdin.readline

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

ans = 0
for i in range(K):
    tmp = 1
    for j in range(i+K, N, K):
        if T[j] == T[j-K]:
            tmp += 1
        else:
            tmp = -(-tmp // 2)
            if T[j-K] == "r":
                tmp *= P
            elif T[j-K] == "s":
                tmp *= R
            else:
                tmp *= S
            ans += tmp
            tmp = 1

        if j + K >= N:
            tmp = -(-tmp // 2)
            if T[j] == "r":
                tmp *= P
            elif T[j] == "s":
                tmp *= R
            else:
                tmp *= S
            ans += tmp
    if i + K >= N:
        if T[i] == "r":
            tmp *= P
        elif T[i] == "s":
            tmp *= R
        else:
            tmp *= S
        ans += tmp

print(ans)
