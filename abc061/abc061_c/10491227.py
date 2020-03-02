N, K = map(int, input().split())
ab = [tuple(map(int, input().split())) for i in range(N)]

ab.sort()

id = 0
for a, b in ab:
    if id + b >= K:
        print(a)
        break
    else:
        id += b
