H,W=map(int,input().split())
a=[[0]*H for i in range(3)]

for i in range(H):
  x=input()
  for y in x:
    if y=="W":
      a[0][i]+=1
    elif y == "B":
      a[1][i]+=1
    else:
      a[2][i]+=1

ans=H*W
for i in range(1,H-1):
  for j in range(i+1,H):
    tmp = i*W - sum(a[0][:i])
    tmp += (j-i)*W - sum(a[1][i:j])
    tmp += (H-j)*W - sum(a[2][j:])

    if tmp<ans:
      ans=tmp
print(ans)
