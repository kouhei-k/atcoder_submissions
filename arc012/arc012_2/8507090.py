N,va,vb,L=map(int,input().split())

t=0
takahashi=0
kame=L
for i in range(N):
  t=(kame-takahashi)/va
  takahashi=kame
  kame+=vb*t
print(abs(kame-takahashi))
