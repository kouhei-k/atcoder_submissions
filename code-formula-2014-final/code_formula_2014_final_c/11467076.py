S = list(input().split())
d = set()

for x in S:
    tmp = ""
    for y in x.split("@")[1:]:
        if y:
            d.add(y)

d = list(d)
d.sort()
print(*d, sep="
")
