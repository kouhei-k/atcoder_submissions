import collections
N = int(input())
A = list(map(int, input().split()))


table = collections.defaultdict(int)
for x in A:
    table[x] += 1
    if table[x] > 1:
        print("NO")
        exit(0)
print("YES")
