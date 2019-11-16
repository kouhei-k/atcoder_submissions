import math
N = int(input())
xy = [tuple(map(int, input().split())) for i in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        if i == j:
            continue
        else:
            ans += ((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2)**0.5

print(ans*math.factorial(N-2)*(N-1) / math.factorial(N) * 2)
