N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        # 4/N - 1/h - 1/n = 1/w
        # (4hn - Nn - Nh) / nhN = 1/w
        # w = nhN / (4hn - Nn - Nh)

        if (4*h*n - N*(n + h)) > 0 and (n*h*N) % (4*h*n - N*(n + h)) == 0:
            w = (n*h*N) // (4*h*n - N*(n + h))
            print(h, n, w)
            exit(0)
