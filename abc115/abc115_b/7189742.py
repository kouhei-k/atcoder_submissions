N = int(input())
p = [0] * N
for i in range(N):
  p[i]=int(input())
  
p = sorted(p,reverse=True)
ans = p.pop(0) / 2 +sum(p)
print(int(ans))
