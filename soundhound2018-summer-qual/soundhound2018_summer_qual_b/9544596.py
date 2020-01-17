S=input()
k=int(input())
ans=[]
for i in range(0,len(S),k):
  ans.append(S[i])
print("".join(ans))
