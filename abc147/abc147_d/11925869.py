def main():
    N = int(input())
    A = list(map(int, input().split()))

    M = max(A)
    L = M.bit_length()
    ans = 0
    mod = 10**9 + 7
    k = [0]*max(1, L)
    k[0] = 1
    for i in range(1, L):
        k[i] = k[i-1]*2
    for j in range(L):
        count = 0
        for x in A:
            if (x >> j) % 2 == 1:
                count += 1
        ans += count*(N - count)*k[j]
    ans %= mod
    print(ans)


main()
