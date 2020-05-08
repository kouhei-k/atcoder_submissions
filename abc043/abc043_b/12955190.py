s = input()
ans = []
for x in s:
    if x != 'B':
        ans.append(x)
    else:
        if ans:
            ans.pop()

print(''.join(ans))
