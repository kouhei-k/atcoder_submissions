r, c = map(int, input().split())
r2, c2 = map(int, input().split())


def check3(a, b, c, d):
    for i in range(c-2, c+3):
        for j in range(d-2, d+3):
            if i+j == a+b or i-j == a-b:
                return(True)
    if c+3 + d == a+b or c-3 + d == a+b or c+3 - d == a - b or c - d + 3 == a-b:
        return(True)
    return(False)


if r == r2 and c == c2:
    print(0)
elif r+c == r2+c2 or r - c == r2 - c2 or abs(r-r2) + abs(c-c2) <= 3:
    print(1)
elif check3(r, c, r2, c2) or (r2-c2 - r - c) % 2 == 0:
    print(2)
else:
    print(3)
