x, y, W = input().split()
c = [list(input()) for i in range(9)]
x = int(x) - 1
y = int(y) - 1

s = set()
for z in W:
    s.add(z)

ans = []

for i in range(4):
    ans.append(c[y][x])
    if "R" in s:
        x += 1
    elif "L" in s:
        x -= 1
    if "U" in s:
        y -= 1
    elif "D" in s:
        y += 1

    if x >= 9:
        s.remove("R")
        s.add("L")
        x -= 2
    elif x < 0:
        s.remove("L")
        s.add("R")
        x += 2
    if y >= 9:
        s.remove("D")
        s.add("U")
        y -= 2
    elif y < 0:
        s.remove("U")
        s.add("D")
        y += 2


print("".join(map(str, ans)))
