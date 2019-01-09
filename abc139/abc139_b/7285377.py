A, B = map(int, input().split())

if B == 1:
    print(0)
    exit(0)
n = 0
x = 1
while(1):
    if x >= B:
        print(n)
        exit(0)
    else:
        x += A - 1
        n += 1
