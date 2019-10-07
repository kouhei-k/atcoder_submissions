import collections
S=input()
T=input()
tableS=collections.defaultdict(list)
tableT=collections.defaultdict(list)

for i in range(len(S)):
  tableS[S[i]].append(i)
  tableT[T[i]].append(i)
listS=tableS.values()
listT=tableT.values()

for x in listS:
  flag=False
  for y in listT:
    if x in y or x in listT:
      flag=True
      break
  if not flag:
    print("No")
    exit(0)
print("Yes")
      
