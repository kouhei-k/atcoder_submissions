N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for i in range(M)]

first = set()
second = set()
for a, b in ab:
    if a == 1:
        first.add(b)
    elif b == N:
        second.add(a)

if len(first & second):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
