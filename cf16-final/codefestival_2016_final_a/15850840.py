H,W = map(int, input().split())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(H):
  for j,x in enumerate(input().split()):
    if x == 'snuke':
      ret = alpha[j] + str(i+1)
      print(ret)
