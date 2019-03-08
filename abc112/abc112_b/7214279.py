N,T=map(int,input().split())
ct = [[0,0] for i in range(N)]
for i in range(N):
  ct[i]=list(map(int,input().split()))
ct.append([-1,T])
ct.sort(key=lambda x:x[1])
index = ct.index([-1,T])
if index==0:
  print("TLE")
else:
  ans = sorted(ct[:index],key=lambda x:x[0])
  print(ans[0][0])
