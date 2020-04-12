N = int(input())
while(N > 0):
    if N % 10 == 7:
        print("Yes")
        exit(0)
    else:
        N = N // 10
print("No")
