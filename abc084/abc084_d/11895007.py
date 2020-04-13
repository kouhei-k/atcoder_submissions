Q = int(input())
lr = [tuple(map(int, input().split())) for i in range(Q)]


def primes(n):
    ret = []
    A = [i for i in range(2, n+1)]
    k = 0
    s = n**0.5
    while(k < s):
        ret.append(A[0])
        k = A[0]
        A = [x for x in A if x % k]
    ret += A
    return ret


prime = primes(10**5)

prime_s = set(prime)
t = [0]*(10**5 + 1)
for i in range(1, 10**5+1):
    if i in prime_s and (i+1)//2 in prime_s:
        t[i] = 1
for i in range(1, 10**5+1):
    t[i] = t[i] + t[i-1]

for l, r in lr:
    print(t[r] - t[l-1])
