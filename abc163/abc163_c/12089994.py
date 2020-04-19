N = int(input())
A = list(map(int, input().split()))

D = [0]*N

for x in A[::-1]:
    D[x-1] += 1

print(*D, sep="
")
