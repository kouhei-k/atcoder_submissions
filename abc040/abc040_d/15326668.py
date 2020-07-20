N,M=map(int,input().split())
aby=[tuple(map(int,input().split())) for i in range(M)]
Q=int(input())

aby.sort(key = lambda x:x[2],reverse=True)

class unionFind:
    parent = []
    count=[]

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.count= [1]*N
    def root(self, x):
        if self.parent[x] == x:
            return(x)
        else:
            self.parent[x] = self.root(self.parent[x])
            return(self.parent[x])

    def same(self, x, y):
        x, y = x-1, y-1
        return(self.root(x) == self.root(y))

    def unite(self, x, y):
        x, y = x-1, y-1
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            self.parent[x] = y
            self.count[y] += self.count[x]
            self.count[x]=self.count[y]
            return
    def getCount(self,x):
      x -=1
      self.count[x] = self.count[self.root(x)]
      return(self.count[x])
G=unionFind(N)
vwi=[[0,0,0]for i in range(Q)]
for i in range(Q):
  v,w=map(int,input().split())
  vwi[i]=[v,w,i]

vwi.sort(key = lambda x:-x[1])
y=0
ans=[0]*Q
id = 0
for v,w, i in vwi:
  while(id < M and aby[id][2]>w):
    a,b,Y = aby[id]
    G.unite(a,b)
    id+=1
  ans[i]=G.getCount(v)
print(*ans,sep="
")
