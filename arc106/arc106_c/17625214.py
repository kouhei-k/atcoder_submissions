N, M = map(int, input().split())

if M == 0:
    for i in range(1, N*2+1, 2):
        print(i, i+1)
elif M > 0:
    if M + 2 > N:
        print(-1)
    else:
        print(1, (M+1)*2 + 2)
        for i in range(1, (M+1)*2 + 1, 2):
            print(1+i, 2+i)
        k = 0
        for i in range(N - (M+2)):
            print((M+1)*2 + 3+k, (M+1)*2 + 4 + k)
            k += 2

else:
    print(-1)
