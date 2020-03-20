N = int(input())


def divisors(n):
    ret = set()
    for i in range(1, int(n**(0.5))+1):
        if n % i == 0:
            ret.add(i)

    return(ret)


ans = N-1
for x in divisors(N):
    ans = min(ans, x-1+(N//x)-1)

print(ans)
