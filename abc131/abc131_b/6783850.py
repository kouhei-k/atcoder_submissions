N,L=map(int,input().split())
if L >= 0:
  print(int((N-1)/2*(L + L + N)))
else:
  if L + N - 1 >= 0: 
    print(int(N / 2 * (L + L + N - 1)))
  else:
    print(int((N - 1)/ 2 * (L + L + N - 2)))
