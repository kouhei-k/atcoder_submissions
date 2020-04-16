def primes(n):
    ret = []
    A = [i for i in range(2, n+1)]
    k = 2**0.5
    s = n**0.5
    while(k < s):
        ret.append(A[0])
        k = A[0]
        A = [x for x in A if x % k]
    ret += A
    return ret


print(len(primes(int(input())-1)))
