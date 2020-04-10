import math
from itertools import permutations
N = int(input())
xy = [tuple(map(int, input().split())) for i in range(N)]

ans = 0
for x in permutations(range(N)):
    for i in range(N-1):
        ans += ((xy[x[i+1]][0] - xy[x[i]][0])**2 +
                (xy[x[i+1]][1] - xy[x[i]][1])**2) ** (1/2)

print(ans / math.factorial(N))
