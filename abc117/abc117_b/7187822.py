N = int(input())
L=list(map(int,input().split()))

L = sorted(L,reverse=True)
if L.pop(0) < sum(L):
  print("Yes")
else:
  print("No")
