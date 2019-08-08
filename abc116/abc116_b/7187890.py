import collections
s=int(input())
count=1
ans=s
prev=0
counter = collections.defaultdict(int)
counter[ans]=1
while(1):
  count+=1
  if ans % 2 == 0:
    ans = ans / 2
  else:
    ans = 3*ans+1
    
  if ans not in counter.keys():
    counter[ans]=count
  else:
    print(count)
    break
