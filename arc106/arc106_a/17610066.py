N = int(input())
A = 1
ans = -1

for i in range(100):
    A *= 3
    if A > N:
        break
    B = 1
    for j in range(100):
        B *= 5
        if A+B > N:
            continue
        elif A+B == N:
            print(i+1, j+1)
            exit(0)
print(ans)
