N=int(input())
S=0
K=N
while K != 0:
  S+=K%10
  K //= 10

if N % S == 0:
  print("Yes")
else:
  print("No")
