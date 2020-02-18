L=int(input())
B=[int(input()) for i in range(L)]
m = max(B)
k = len(bin(m))-2
A= 0
for i in range(k):
  tmp=0
  tmp2=1
  for j in range(1,L):
    tmp=tmp ^ ((B[j-1]>>i)%2)
    tmp2=tmp2^((B[j-1]>>i)%2)
  if tmp ^((B[L-1]>>i)%2) == 0:
    continue
  elif tmp2 ^((B[L-1]>>i)%2)==1:
    A+=1<<i
  else:
    print(-1)
    exit(0)
print(A)
tmp=A
for i in range(L-1):
  tmp=B[i]^tmp
  print(tmp)


    
    
 
