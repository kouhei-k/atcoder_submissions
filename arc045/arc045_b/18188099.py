N,M=map(int,input().split())
S=[[0,0] for i in range(M)]
A=[0]*(N+1)
for i in range(M):
  s,t=map(int,input().split())
  s-=1
  S[i][0]=s
  S[i][1]=t
  A[s]+=1
  A[t]-=1
AS=[0]*(N+1)
for i in range(N):
  AS[i+1]=AS[i]+A[i]

class segment_tree:
    n = 0
    segtree = []
    max_v = 10**10

    def __init__(self, A, max_n=2**31 - 1):
        self.N = len(A)
        self.max_v = max_n
        self.n = (self.N-1).bit_length()
        self.n = 2 ** self.n
        self.segtree = [max_n]*(2*self.n)
        for i in range(self.N):
            self.segtree[self.n+i - 1] = A[i]
        for i in range(self.n - 2, -1, -1):
            self.segtree[i] = min(self.segtree[i*2 + 1], self.segtree[i*2 + 2])

    def update(self, i, x):
        id = self.n+i - 1
        self.segtree[id] = x
        while(id > 0):
            id = (id - 1) // 2
            self.segtree[id] = min(
                self.segtree[id*2 + 1], self.segtree[id*2+2])
            #print(self.segtree[id*2 + 1], self.segtree[id*2+2])


    def query(self, a, b, k, l, r):
		#a < bじゃないとmax_vが返ってしまうので、 A_a から A_bまでをやりたいときはb+1を使う
        if r <= a or l >= b:
            return(self.max_v)
        if a <= l and r <= b:
            return(self.segtree[k])
        else:
            vl = self.query(a, b, k*2+1, l, (l+r)//2)
            vr = self.query(a, b, k*2+2, (l+r)//2, r)
            return(min(vl, vr))



n = (N).bit_length()
n = 2 ** n
A = [2**31 - 1]*n
ans=[]
G = segment_tree(AS)
for i in range(M):
    s,t=S[i]
    
    if G.query(s+1, t+1, 0, 0, n)>1:
      ans.append(i+1)
    
print(len(ans))
for x in ans:
  print(x)
