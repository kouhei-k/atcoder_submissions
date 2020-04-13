import math
A, B, K = map(int, input().split())


def divisors(n):
    ret = set()
    for i in range(1, math.ceil(n**0.5) + 1):
        if n % i == 0:
            ret.add(i)
            ret.add(n//i)
    return ret


a = sorted(list(divisors(A) & divisors(B)))
print(a[-K])
