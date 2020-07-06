def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    plus = [A[i] for i in range(N) if A[i] >= 0]
    minus = [A[i] for i in range(N) if A[i] < 0]

    ans = 1

    P = len(plus)
    M = len(minus)
    plus.sort(reverse=True)
    minus.sort()
    mod = 10**9 + 7

    if N == K:
        for x in A:
            ans *= x
            ans %= mod
    elif P == 0:
        if K % 2 == 1:
            minus.sort(reverse=True)
        for i in range(K):
            ans *= minus[i]
            ans %= mod
    else:  # 必ず正の値が作れる？ 1つ以上余るので、偶奇は選べるはず
        id = 0
        if K % 2 == 1:
            ans = plus[0]
            id = 1
            P -= 1
            K -= 1
        pp = [plus[i] * plus[i+1] for i in range(id, P-1+id, 2)]
        mm = [minus[i] * minus[i+1] for i in range(0, M-1, 2)]

        id = 0
        id2 = 0

        for i in range(K // 2):
            if id < P // 2 and (id2 >= M // 2 or pp[id] >= mm[id2]):
                ans *= pp[id]
                id += 1
            else:
                ans *= mm[id2]
                id2 += 1
            ans %= mod

    print(ans % mod)


main()
