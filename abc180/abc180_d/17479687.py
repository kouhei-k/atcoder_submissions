X, Y, A, B = map(int, input().split())
exp = 0
while(X < Y):
    if X*A < X+B:
        if X*A >= Y:
            break
        else:
            X *= A
            exp += 1
    else:
        exp += (Y-1 - X) // B
        break

print(exp)
