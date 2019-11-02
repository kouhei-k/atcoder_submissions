import collections
N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))


table = collections.defaultdict(int)

if a in P or b in P:
    print("NO")
else:
    for x in P:
        table[x] += 1
        if table[x] > 1:
            print("NO")
            exit(0)
    print("YES")
