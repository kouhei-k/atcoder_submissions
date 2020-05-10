A, B, C, K = map(int, input().split())
if A >= K:
    print(K)
else:
    ans = A - max(0, (K - (A+B)))
    print(ans)
