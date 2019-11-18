import collections
N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

if N < M:
    print("NO")
    exit(0)
tableD = collections.defaultdict(int)
tableT = collections.defaultdict(int)
for i in range(N):
    tableD[D[i]] += 1
for i in range(M):
    tableT[T[i]] += 1

for x in tableT:
    if tableD[x] >= tableT[x]:
        continue
    else:
        print("NO")
        exit(0)
print("YES")
