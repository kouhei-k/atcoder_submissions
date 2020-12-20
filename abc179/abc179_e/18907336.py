N, X, M = map(int, input().split())

ans = 0
s = [0]*(M+1)
prev = X
A = 0
if N > M+1:
    ans = X
    for i in range(M+1):
        A = (prev**2) % M
        if s[A-1] > 0:
            N -= i+1
            break
        else:
            s[A-1] = ans
            ans += A
        prev = A

    x = A**2 % M
    count = 1
    su = A
    while(x != A):
        su += x
        x = x ** 2 % M
        count += 1

        if count == N:
            break

    ans += su*(N//count)
    N %= count
    for i in range(N):
        ans += A
        A = A**2 % M


else:
    for i in range(N):
        ans += X
        X = X**2 % M

print(ans)
