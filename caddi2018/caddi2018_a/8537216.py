import math
N, P = map(int, input().split())
p = P**(1/N)
ans = 1
flag=False
if N==1:
  print(P)
  exit(0)


divisors=[]

for i in range(2,round(P**(1/N))+1):
  if P%i==0:
    divisors.append(i)
for i in reversed(divisors):
    if P % (i ** N) == 0:
        ans = i
        break
print(ans)
