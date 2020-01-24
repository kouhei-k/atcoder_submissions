P=float(input())
import math
import decimal
R= max(0,(math.log(P,2)*1.5+1))
L= 0
m=0
while(1):
  if math.ceil(R*10**10)==math.ceil(L*10**10):
    m=math.ceil(R*10**10) * 10**(-10)
    break
  m= (R+L)/2
  tmp= 2**(m/1.5)
  tmp = P/tmp
  l=(L+m)/2
  tmp2=2**(l/1.5)
  tmp2=P/tmp2
  if tmp2 + l <tmp + m:
    R=m
    continue
  else:
    L=l
  r = (R+m)/2
  tmp3=2**(r/1.5)
  tmp3=P/tmp3
  if tmp3 + r < tmp+m:
    L=m
  else:
    R=r
print(m+ (P/(2**(m/1.5))))
