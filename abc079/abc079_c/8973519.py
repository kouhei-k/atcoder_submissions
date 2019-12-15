abcd=list(input())
abcd=list(map(int,abcd))
for i in range(2**3):
  ret=abcd[0]
  for j in range(3):
    if (i>>j)%2==1:
      ret-=abcd[j+1]
    else:
      ret+=abcd[j+1]
  if ret==7:
    ans=[str(abcd[0])]
    for j in range(3):
      if (i>>j)%2==1:
        ans.append("-")
      else:
        ans.append("+")
      ans.append(str(abcd[j+1]))
    ans.append("=")
    ans.append("7")
    print("".join(ans))
    exit(0)
