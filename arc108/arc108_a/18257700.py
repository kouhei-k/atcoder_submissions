S, P = map(int, input().split())
ans = 0
for i in range(1, 10**6+1):
    if P % i == 0:
        j = P // i
        if i + j == S:
            print("Yes")
            exit(0)

print("No")
