N,L=map(int,input().split())
graph=[[" "]*(L-1) for i in range(L)]
for i in range(L):
  graph[i] = list(input())
  
l=input().index("o")
graph=graph[::-1]
for i in range(L):
  if l>1 and graph[i][l-1] == "-":
    l=l-2
  elif l<2*N-2 and graph[i][l+1]=="-":
    l=l+2
print(l//2 +1)
