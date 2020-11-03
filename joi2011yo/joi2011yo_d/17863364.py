N = int(input())
A = list(map(int, input().split()))
D = [[0]*21 for i in range(N-1)]

D[0][A[0]] = 1


for i in range(N-2):
    for j in range(21):
        if j + A[i+1] <= 20:
            D[i+1][A[i+1] + j] += D[i][j]
        if j - A[i+1] >= 0:
            D[i+1][j - A[i+1]] += D[i][j]

print(D[N-2][A[-1]])
