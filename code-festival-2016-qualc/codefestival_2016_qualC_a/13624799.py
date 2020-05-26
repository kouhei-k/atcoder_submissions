S = input()
id = -1
if 'C' in S:
  id = S.index('C')
  if 'F' in S[id:]:
    print("Yes")
  else:
    print("No")
else:
  print("No")
