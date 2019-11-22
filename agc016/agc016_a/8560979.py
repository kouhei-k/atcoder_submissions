alphabet = "abcdefghijklmnopqrstuvwxyz"

s = input()
ans = 100
for target in alphabet:
    if target not in s:
        continue

    indexes = []
    for i in range(len(s)):
        if s[i] == target:
            indexes.append(i)
    tmp = 0
    tmp = max(indexes[0], (len(s)-1) - indexes[-1])

    for i in range(len(indexes)-1):
        tmp = max(tmp, (indexes[i+1]-1) - indexes[i])

    ans = min(ans, tmp)

print(ans)
