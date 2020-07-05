N = int(input())
if N % 1000 == 0:
    print(0)
else:
    d = N % 1000
    print(1000 - d)
