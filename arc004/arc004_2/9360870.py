N=int(input())
d=[int(input()) for i in range(N)]

print(sum(d))

if N==1:
  print(d[0])
else:
  if max(d)*2<=sum(d):
    print(0)
  else:
    print(max(d)*2-sum(d))
    
