a, b, x, y = map(int, input().split())
if 2*x >= y:
    if a > b:
        print(x + (a-1 - b)*y)

    else:
        print((b-a)*y + x)
else:
    if a > b:
        print(((a - b-1)*2 + 1)*x)
    else:
        print(x + (b-a)*2*x)
