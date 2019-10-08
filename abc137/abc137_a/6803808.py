A,B = map(int,input().split())
if B >= 0:
  print(max(A*B,A+B))
else:
  print(max(A*B,A-B))
