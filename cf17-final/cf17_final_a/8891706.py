S=list(input())
A="AKIHABARA"
id=0
for i in range(len(A)):
  if len(S) > i and A[i]==S[i]:
    continue
  else:
    if A[i]=="A":
      S.insert(i,"A")
    else:
      print("NO")
      exit(0)
if "".join(S)==A:
  print("YES")
else:
  print("NO")
