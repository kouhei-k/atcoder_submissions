def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append((i,n//i))
            if i != n // i:
                divisors.append((n//i,i))

    # divisors.sort()
    return divisors
N=int(input())
div=make_divisors(N)
ans=float("inf")
for x, y in div:
  ans=min(ans,(x-1)+(y-1))
print(ans)
