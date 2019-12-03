n, m, d = map(int, input().split())
if d == 0:
    print((m-1) * (1/n))
elif d < n:
    # if d * 2 <= n:
    #     print((((2*n-6*d)/n)**(m-1)))
    print((m-1)*(2*n - 2*d)/(n**2))
    # else:
    #     print(((2*n-2*d) / n)**m-1)
else:
    print(0)
