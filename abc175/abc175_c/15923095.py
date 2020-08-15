X, K, D = map(int, input().split())
if abs(X) > D*K:
    print(abs(X) - D*K)

else:
    k = abs(X) // D
    X = abs(X) % D
    K -= k
    if K % 2 == 0:
        print(X)
    else:
        print(D-X)
