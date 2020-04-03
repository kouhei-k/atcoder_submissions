def main():
    import fractions
    import math
    A, B = map(int, input().split())

    gcd = fractions.gcd(A, B)

    tmp = gcd
    ans = 1
    for i in range(2, int(-(-gcd**0.5//1))+1):
        if tmp % i == 0:
            ans += 1
            while(tmp % i == 0):
                tmp = tmp//i
    if tmp != 1:
        ans += 1
    print(ans)


main()
