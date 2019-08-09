N,H=map(int,input().split())
ab=[[0]*2 for i in range(N)]
for i in range(N):
  ab[i]=list(map(int,input().split()))
ab.sort(key=lambda x:x[0])
max_katana=ab[-1]
ab.sort(reverse=True,key=lambda x:x[1])
count=0
for i in range(N):
  if H > 0:
    if ab[i][1] >= max_katana[0]:
      H -= ab[i][1]
      count+=1
    else:
      break
if H > 0:
  if H % max_katana[0]==0:
    count+= H // max_katana[0]
  else:
    count+= (H // max_katana[0]) + 1
print(count)
