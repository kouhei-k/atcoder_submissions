N, W, K, V = map(int, input().split())
cv = [tuple(map(int, input().split())) for i in range(N)]

for i in range(N):
  print(i%W)
