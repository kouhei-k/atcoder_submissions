S=list(input().split())
ans=[""]*len(S)
for i in range(len(S)):
  if S[i]=="Right":
    ans[i]=">"
  elif S[i]=="Left":
    ans[i]="<"
  elif S[i]=="AtCoder":
    ans[i]="A"
print(" ".join(ans))
