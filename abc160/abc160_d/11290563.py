def main():
    N, X, Y = map(int, input().split())

    ans = [0]*(N-1)

    for i in range(1, N):
        for j in range(i+1, N+1):
            if j <= X or Y <= i:
                tmp = j - i
            elif i <= X and j <= Y:
                tmp = (X - i) + min(j - X, Y - j + 1)
            elif i <= X and Y <= j:
                tmp = (X - i) + (j - Y) + 1
            elif i <= Y and Y <= j:
                tmp = (j - Y) + min(Y - i, i - X + 1)
            else:
                tmp = min(j - i, i - X + Y - j + 1)

            ans[tmp - 1] += 1

    print(*ans, sep="
")


main()
