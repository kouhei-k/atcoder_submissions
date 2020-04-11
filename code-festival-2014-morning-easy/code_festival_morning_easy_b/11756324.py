n = int(input())
if n % 40 == 0 or n % 40 > 20:
    if n % 40 == 0:
        print(1)
    else:
        k = n % 40 - 20
        print(20 - k + 1)
else:
    print(n % 40)
