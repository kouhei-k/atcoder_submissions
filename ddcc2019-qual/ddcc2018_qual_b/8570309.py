N = int(input())

if N % 2 == 0:
    n = (N // 2) - 1
    print(n*(n+1)*2)
else:
    n = (N // 2)
    ans = (n-1) + 0.25
    ans += (n-1)*(n-2)//2
    ans = int(ans*4)
    print(ans)
