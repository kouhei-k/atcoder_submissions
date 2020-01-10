from fractions import gcd
N, M = map(int, input().split())
a = list(map(int, input().split()))
k = a[0]
for i in range(1, N):
    k = (a[i]*k) // gcd(a[i], k)
    if k > M*2:
        print(0)
        exit(0)
    k = int(k)
ans = (M - (k // 2)) // k

if M >= (k // 2):
    flag = True
    for i in range(N):
        if (k // a[i]) % 2 == 0:
            print(0)
            exit(0)
    if flag:
        ans += 1

print(int(ans))
