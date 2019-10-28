a, b, c = map(int, input().split())
if a != b:
    if a != c and b != c:
        print(3)
    else:
        print(2)
else:
    if a != c and b != c:
        print(2)
    else:
        print(1)
