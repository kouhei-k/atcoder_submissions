def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    SS = [0]*(N+1)
    for i in range(N):
        SS[i+1] = SS[i] + S[i+1]
    M = 0
    for i in range(N):
        start = SS[i]
        if M < S[i+1]:
            M = S[i+1]
        if ans < M + start:
            ans = M + start
    print(ans)


main()
