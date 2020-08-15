def main():
    import sys
    input = sys.stdin.buffer.readline
    N, K = map(int, input().split())
    P = tuple(map(lambda x: int(x) - 1, input().split()))
    C = tuple(map(int, input().split()))
    ans = -10**18

    for i in range(N):
        k = K
        D = [[0, 0] for i in range(N)]
        x = i
        X, Y = 0, 0
        count = 0
        score = 0
        for j in range(K):
            if D[P[x]][0] == 0:
                score += C[P[x]]
                D[P[x]][0] = score
                D[P[x]][1] = count
                x = P[x]
                count += 1
            else:
                X = D[P[x]][0] - C[P[x]]
                score -= X
                L = (count - D[P[x]][1])
                k -= D[P[x]][1]

                score *= (k // L) - 1
                l = (K % L) + L
                score += X
                ans = max(ans, score)
                for _ in range(l):
                    score += C[P[x]]
                    ans = max(ans, score)
                    x = P[x]

                break
            if score > ans:
                ans = score
    print(ans)


main()
