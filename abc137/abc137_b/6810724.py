K,X = map(int,input().split())

ans = []
for i in reversed(range(K)):
    ans.append(X - i)

for i in range(1,K):
    ans.append(X + i)
print(" ".join(map(str, ans)))
  
