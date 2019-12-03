N, Z, W = map(int, input().split())
a = list(map(int, input().split()))
if N > 1:
    print(max(abs(W-a[-1]), abs(a[-1] - a[-2])))
else:
    print(abs(W - a[0]))
