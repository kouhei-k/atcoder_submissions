N,K = map(int, input().split())
w = 0
for i in range(N):
  w += int(input())
  if w >= K:
    print(i+1)
    exit(0)
