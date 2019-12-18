x, y, W = input().split()
x, y = int(x), int(y)
c = [list(input()) for i in range(9)]
W = set(list(W))
ans = []
for _ in range(4):
    ans.append(str(c[y-1][x-1]))
    tmp = set()

    if "R" in W:
        if x == 9:
            W.remove("R")
            W.add("L")
            x -= 1
        else:
            x += 1
    elif "L" in W:
        if x == 1:
            W.remove("L")
            W.add("R")
            x += 1
        else:
            x -= 1
    if "U" in W:
        if y == 1:
            y += 1
            W.remove("U")
            W.add("D")
        else:
            y -= 1
    elif "D" in W:
        if y == 9:
            y -= 1
            W.remove("D")
            W.add("U")
        else:
            y += 1

print("".join(ans))
