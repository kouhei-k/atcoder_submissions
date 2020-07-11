def main():
    N = int(input())

    ans = [0]*N
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                res = i**2 + j ** 2 + k**2 + i*j + j*k + k*i
                if res > N:
                    continue
                else:
                    ans[res-1] += 1

    for i in range(N):
        print(ans[i])


main()
