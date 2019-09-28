from math import sqrt, ceil
import fractions
A, B = map(int, input().split())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors


ans = 1

tmp = make_divisors(fractions.gcd(A, B))

for x in tmp:
    if is_prime(x):
        ans += 1

print(ans)
