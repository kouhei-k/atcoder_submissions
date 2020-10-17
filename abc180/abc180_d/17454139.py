X, Y, A, B = map(int, input().split())
exp = 0
while(X * (A-1) < B and X*A < Y):
    X *= A
    exp += 1

k = max(Y-1-X, 0)

exp += k // B


print(exp)
