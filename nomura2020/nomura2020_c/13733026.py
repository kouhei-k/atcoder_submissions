import math
N = int(input())
A = list(map(int, input().split()))

G = []
nodes = [0]*(N+1)
nodes[0] = 1
for i in range(N):
    nodes[i+1] = nodes[i]*2

if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit(0)

ans = 0
node = 1 - A[0]
nodes = [0 for i in range(N)]
nodes[0] = 1 - A[0]  # 深さi-1で、葉でない頂点の個数の最小値、最大値

# 可能性の判定 + 深さNの確定
for i in range(1, N+1):
    if i == N:
        if math.ceil(A[i]/2) > nodes[i-1]:
            print(-1)
            exit(0)
        else:
            continue
    else:
        # 自分の深さが可能かの判定
        if nodes[i-1] * 2 >= A[i]:
            nodes[i] = nodes[i-1] * 2 - A[i]
        else:
            print(-1)
            exit(0)
ans += A[i]
prev = A[-1]
for i in range(N-1, -1, -1):
    # その深さでできる最大値
    prev = min(nodes[i], prev) + A[i]
    ans += prev

print(ans)
