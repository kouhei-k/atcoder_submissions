X, Y = map(int, input().split())

for i in range(X+1):
    j = X - i
    if 2*i + 4*j == Y:
        print("Yes")
        exit(0)
print("No")
