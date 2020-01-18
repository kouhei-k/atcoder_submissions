a, b, c, d = map(int, input().split())

ans = set()
ans.add(a)
ans.add(b)
ans.add(c)
ans.add(d)

if 1 in ans and 9 in ans and 7 in ans and 4 in ans:
    print("YES")
else:
    print("NO")
