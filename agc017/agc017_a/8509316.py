from math import factorial
N,P=map(int,input().split())
a=list(map(int,input().split()))
odd=0
even=0
for i in range(N):
  if a[i]%2==0:
    even+=1
  else:
    odd+=1
ans=2**even
k=0
if P==0:
  k=0
else:
  k=1
tmp=0
for i in range(k,odd+1,2):
  tmp+=factorial(odd)//factorial(odd-i)//factorial(i)

print(ans*tmp)
