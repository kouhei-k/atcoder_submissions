N = int(input())
if N % 4 == 0 or N % 7 == 0:
    print("Yes")
    exit(0)
else:
    for _ in range(N // 4):
        N -= 4
        if N % 7 == 0:
            print("Yes")
            exit(0)

print("No")
