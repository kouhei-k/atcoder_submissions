N=int(input())
s=list(input())
for i in range(2**2):
  sw=[1,1]
  ans=[1]*(N+1)
  for j in range(2):
    if (i>>j)%2==1:
      sw[j]=0
      ans[j]=0
  for j in range(1,N):
    if sw[1]== 1:
      if s[j]=="o":
        sw[0],sw[1]=sw[1],sw[0]
      else:
        sw[0],sw[1]=sw[1],(sw[0])^1
    else:
      if s[j]=="o":
        sw[0],sw[1]=sw[1],(sw[0])^1
      else:
        sw[0],sw[1]=sw[1],sw[0]
    ans[j+1]=sw[1]
  
  if ans[0]==ans[N]:
    if ans[0]==1:
      if s[0]=="o":
        if ans[N-1]!=ans[1]:
          continue
      else:
        if ans[N-1]==ans[1]:
          continue
    else:
      if s[0]=="o":
        if ans[N-1]==ans[1]:
          continue
      else:
        if ans[N-1]!=ans[1]:
          continue
    for i in range(N):
      if ans[i]==1:
        ans[i]="S"
      else:
        ans[i]="W"
    print("".join(ans[:N]))
    exit(0)
  else:
    continue
print(-1)
