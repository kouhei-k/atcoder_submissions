n = int(input())
d = dict()
for i in range(n):
    a, b = input().split()
    d[a] = b
ans = []
m = int(input())
for i in range(m):
    x = input()
    if x in d:
        ans.append(d[x])
    else:
        ans.append(x)
print("".join(ans))
