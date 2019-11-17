N,A,B=map(int,input().split())
if A>B or (N<2 and A!=B):
  print(0)
  exit(0)
min=A*(N-1)+B
max=A+B*(N-1)

print(max-min + 1)
