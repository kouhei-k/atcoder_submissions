S = input()

t = 1
prev = 0
ans = 0
for i, x in enumerate(S):

    if x == '*':
        continue
    elif x == '+':
        if t != 0:
            ans += 1
        t = 1
    else:
        t *= int(x)
if t != 0:
    ans += 1

print(ans)
