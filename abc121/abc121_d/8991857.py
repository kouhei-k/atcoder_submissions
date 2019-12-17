A,B=map(int,input().split())
k=len(bin(B))-2
ans=0
for i in range(k):
  diff=(B- max(2**i,A))
  t=2**(i+1)
  l=2**i
  tmp=((diff+1)//t)*l
 
  C=max(A,l)+tmp*t - 1
  if B%t >= C%t:
    tmp+= max(0,(B%t -(l-1)) - max(0,(C%t-(l-1))))
  else:
    tmp+= max(0,B%t-(l-1)) +(min(l,t-1-C%t))
  if tmp%2==1:
    ans+=2**i
print(ans)
