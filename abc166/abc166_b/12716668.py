import bisect
N, K = map(int, input().split())
D = [0]*N
for i in range(K):
    d = int(input())
    for x in input().split():
        x = int(x)
        x -= 1
        D[x] += 1

D.sort()
print(bisect.bisect_left(D, 1))
