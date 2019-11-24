N = int(input())
r = input()
gp = 0
for x in r:
    if x == "A":
        gp += 4
    elif x == "B":
        gp += 3
    elif x == "C":
        gp += 2
    elif x == "D":
        gp += 1
print(gp / N)
