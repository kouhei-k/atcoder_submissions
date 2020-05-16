N=int(input())
for i in range(10,10**5):
  arr=[]
  t=i
  while(t>0):
    arr.append(t%10)
    t=t//10
  tmp=0
  for j,x in enumerate(arr):
    tmp+= i**j * x
  if tmp==N:
    print(i)
    exit(0)
print(-1)
