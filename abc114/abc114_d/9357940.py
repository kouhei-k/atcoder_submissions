import collections
import copy
N=int(input())
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

table=collections.defaultdict(int)
for i in range(1,N+1):
  tmp=factorization(i)
  for a,b in tmp:
    table[a]+=b

divisors=[[5,5,3],[15,5],[25,3],[75]]
ans=0
for x in divisors:
  tmp=[set() for i in range(len(x))]
  for i,y in enumerate(x):
    for z in table:
      if table[z]>=y-1:
        tmp[i].add(z)
    if len(tmp[i])==0:
      break
  for y in tmp[0]:
    if len(x)>1:
      for z in tmp[1]:
        if y==z:
          continue
        if len(x)>2:
          if y>z:
            continue
          for w in tmp[2]:
            if z==w or w==y:
              continue
            else:
              ans+=1
        else:
              ans+=1
    else:
      ans+=1
print(ans)
  
