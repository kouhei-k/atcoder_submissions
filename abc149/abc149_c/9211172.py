X = int(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


while(1):
    if is_prime(X):
        print(X)
        break
    else:
        X += 1
