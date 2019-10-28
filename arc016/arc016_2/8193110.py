N=int(input())
x=[list(input()) for i in range(N)]
ans=0
for i in range(9):
  for j in range(N):
    if x[j][i]=="x":
      ans+=1
    elif x[j][i] == "o":
      if j >0:
        if x[j-1][i] != "o":
          ans+=1
      else:
        ans+=1
print(ans)     
