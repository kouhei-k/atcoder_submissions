N = int(input())
a = [tuple(map(int, input().split())) for i in range(N)]
ans = [0]*N
for i in range(3):
  d = dict()
  for j in range(N):
    if a[j][i] in d:
      d[a[j][i]]+=1
    else:
      d[a[j][i]] = 1
  for j in range(N):
    if d[a[j][i]] == 1:
      ans[j] += a[j][i]
print(*ans, sep = '
')
