s = input()
t = input()

sl = len(s)
tl = len(t)

s = set(s)
t = set(t)

flag = False
for x in s:
    for y in t:
        if x < y:
            flag = True
            break
    if flag:
        break

if s == t and sl < tl:
    flag = True

if flag:
    print("Yes")
else:
    print("No")
