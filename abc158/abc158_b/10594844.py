N, A, B = map(int, input().split())

k = N // (A+B)
ans = k * A

s = (A+B)*k

if N - s <= A:
    print(ans + (N - s))
else:
    print(ans + A)
