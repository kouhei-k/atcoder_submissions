S=input()
used=[0,0,0]
for x in S:
  if x=="a" and used[0] == 0:
    used[0]=1
  elif x=="b" and used[1]==0:
    used[1]=1
  elif x=="c" and used[2]==0:
    used[2]=1
  else:
    print("No")
    exit(0)
print("Yes")
