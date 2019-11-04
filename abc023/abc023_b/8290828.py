N=int(input())
S=input()
if N%2 !=1:
  print(-1)

else:
  if S[N//2]=="b":
    for i in range(1,N//2+1):
      a=S[N//2-i]
      b=S[N//2+i]
      if i%3==1:
        if a=="a" and b=="c":
          continue
        else:
          print(-1)
          exit(0)
      if i %3 == 2:
        if a=="c" and b=="a":
          continue
        else:
          print(-1)
          exit(0)
      else:
        if a=="b" and b== "b":
          continue
        else:
          print(-1)
          exit(0)
    print(N//2)
          
  else:
    print(-1)
