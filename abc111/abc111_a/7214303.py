N=list(input())
for x in range(len(N)):
  if N[x]=="1":
    N[x]="9"
  else:
    N[x]="1"
print("".join(N))
