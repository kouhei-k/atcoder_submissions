S=list(map(int,list(input())))
K=int(input())

if S[0]==1:
  if K==1:
    print(1)
  else:
    for i in range(1,len(S)):
      if S[i] != 1:
        print(S[i])
        exit(0)
      if i == K-1:
        print(1)
        exit(0)
else:
  print(S[0])
