from itertools import permutations
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
a = 0
b = 0
flagP = False
flagQ = False
count = 0
for x in permutations(range(1, N+1)):
    count += 1
    if flagP == False:
        for i in range(N):
            if x[i] != P[i]:
                break
            elif i == N-1:
                flagP = True
                a = count
    if flagQ == False:
        for i in range(N):
            if x[i] != Q[i]:
                break
            elif i == N-1:
                flagQ = True
                b = count

    if flagQ and flagP:
        break


print(abs(a-b))
