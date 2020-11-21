N = int(input())
s = input()

q = []
ans = 0
for x in s:
    if x == 'f':
        q.append(1)
    elif x == 'o' and q and q[-1] == 1:
        q[-1] = 2
    elif x == 'x' and q and q[-1] == 2:
        q.pop()
    else:
        ans += 1
        q.append(0)

print(ans+sum(q))
