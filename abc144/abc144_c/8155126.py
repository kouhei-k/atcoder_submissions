N = int(input())


def solve(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append((i + N // i) - 2)

    return min(divisors)


print(solve(N))
