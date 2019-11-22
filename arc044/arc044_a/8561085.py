N = int(input())


def isPrime(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True


if N == 1:
    print("Not Prime")
elif isPrime(N):
    print("Prime")
else:
    tmp = str(N)
    if tmp[-1] != "5" and int(tmp[-1]) % 2 != 0:
        sumN = 0
        for x in tmp:
            sumN += int(x)
        if sumN % 3 != 0:
            print("Prime")
            exit(0)

    print("Not Prime")
