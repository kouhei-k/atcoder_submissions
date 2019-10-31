N,K=map(int,input().split())
T=[list(map(int,input().split())) for i in range(N)]
for i in range(K**N):
  tmp=0
  for j in range(N):
    k = i // (K**j)
    k=k%K
    tmp ^= T[j][k]
  if tmp == 0:
    print("Found")
    exit(0)
    
print("Nothing")
