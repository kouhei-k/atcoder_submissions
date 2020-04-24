ans = []
for i, x in enumerate(input().split()):
    if i > 0 and x:
        ans.append(',')
    ans.append(x)
print("".join(ans))
