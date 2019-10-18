c = [list(input()) for i in range(4)]

for i in reversed(range(4)):
    print(" ".join(list(reversed(c[i]))))
