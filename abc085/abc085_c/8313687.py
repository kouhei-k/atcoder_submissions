N,Y=map(int,input().split())

if Y < N*1000 or Y>N*10000:
  print(-1,-1,-1)
else:
  for i in range(N+1):
    for j in range(N-i+1):
      if 1000*i + 5000*j+ 10000*(N-i-j)==Y:
        print(N-i-j,j,i)
        exit(0)
  print(-1,-1,-1)
