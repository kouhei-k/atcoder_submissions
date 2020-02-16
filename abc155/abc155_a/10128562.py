A, B, C = map(int, input().split())

s = set([A, B, C])

if len(s) == 2:
    print("Yes")
else:
    print("No")
