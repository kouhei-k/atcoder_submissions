import collections
S = input()

s = list(S.split("><"))
ans = 0
for i in range(len(s)):
    table = collections.defaultdict(int)
    for y in s[i]:
        table[y] += 1

    if i == 0 and len(table) != 0:
        table["<"] -= 1
    if i == len(s)-1 and len(table) != 0:
        table[">"] -= 1
    table = list(table.values())
    if len(table) == 2:
        table.sort()
        ans += max((table[1]+1)*(table[1]+2) // 2, 0)
        ans += max((table[0]+1)*table[0] // 2, 0)

    elif len(table) == 1:
        ans += max((table[0]+1)*(table[0]+2) // 2, 0)
    else:
        ans += 1
print(ans)
