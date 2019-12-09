import math
N = int(input())
C = [0]*(N-1)
S = [0]*(N-1)
F = [0]*(N-1)

for i in range(N - 1):
    C[i], S[i], F[i] = map(int, input().split())

times = [0]*N
for j in range(N-1):
    time = 0
    for i in range(j, N-1):
        if time <= S[i]:
            time = S[i]
        else:
            time = math.ceil(time / F[i]) * F[i]
        time += C[i]

    times[j] = time
for i in range(N):
    print(times[i])
