N = int(input())
flag = False
c = 0
for i in range(N):
  a,b = input().split()
  if a == b:
    c += 1
  else:
    c = 0
  if c > 2:
    flag = True
if flag:
  print("Yes")
else:
  print("No")
