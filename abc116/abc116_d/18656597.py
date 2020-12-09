N,K=map(int,input().split())
td=[tuple(map(int,input().split())) for i in range(N)]
td.sort(key=lambda x:x[1],reverse=True)

s=set()
A=[0]

for t,d in td:
  if t not in s:
    s.add(t)
    A.append(A[-1]+d)
s=set()
B=0
id =0
ans=0
x=len(A)-1
for i in range(K):
  t,d= td[i]
  B+=d
  if t not in s:
    id += 1
    s.add(t)
  
  tmp=min(x,id+K-i-1)
  C=A[tmp]-A[id] + B + tmp*tmp
  if C>ans:
    ans=C
print(ans)
