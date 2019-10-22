H,W=map(int,input().split())
s=[list(input()) for i in range(H)]
for i in range(H):
  ans=["0"]*W
  for j in range(W):
    if s[i][j]=="#":
      ans[j]="#"
      continue
    count=0
    if i > 0:
      if s[i-1][j]=="#":
        count+=1
      if j > 0:
        if s[i-1][j-1]=="#":
          count+=1
      if j < W-1:
        if s[i-1][j+1]=="#":
          count+=1
    if i<H-1:
      if s[i+1][j]=="#":
        count+=1
      if j >0:
        if s[i+1][j-1]=="#":
          count+=1
      if j<W-1:
        if s[i+1][j+1]=="#":
          count+=1
    if j>0:
      if s[i][j-1]=="#":
        count+=1
    if j<W-1:
      if s[i][j+1]=="#":
        count+=1
    ans[j]=str(count)
  print("".join(ans))
        
        
