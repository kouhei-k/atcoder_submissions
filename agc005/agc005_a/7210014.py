X = input()
Y = []
for i in X:
    Y.append(i)
    if len(Y) > 1:
        if Y[-2] + Y[-1] == "ST":
            Y.pop()
            Y.pop()
print(len(Y))
