N = int(input())
ans = 0
for i in range(1, N):
  k = (N-1) // i
  ans += k
print(ans)
  
