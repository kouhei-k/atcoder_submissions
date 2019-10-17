import collections
N = int(input())
a = list(map(int, input().split()))


table = collections.defaultdict(int)
for x in a:
    table[x] += 1
ans = 0
for x in table:
    if x < table[x]:
        ans += table[x] - x

    elif x > table[x]:
        ans += table[x]

print(ans)
