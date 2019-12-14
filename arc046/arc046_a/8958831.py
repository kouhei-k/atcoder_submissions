N=int(input())
ans=[]
for _ in range((N-1)//9 +1):
  if N%9!=0:
    ans.append(N%9)
  else:
    ans.append(9)
print("".join(map(str,ans)))
