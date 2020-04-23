def divisors(n):
    ret = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ret.add(i)
            ret.add(n//i)
    return(ret)


def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = set()
    for i in range(N-1, -1, -1):
        a[i] %= 2
        # print(a)
        if a[i]:

            for j in divisors(i+1):
                # print(j-1)
                a[j-1] += 1
            ans.add(i+1)

    print(len(ans))

    print(*ans)


main()
