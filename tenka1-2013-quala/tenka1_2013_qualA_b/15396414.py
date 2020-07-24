N = int(input())
ans = 0
for i in range(N):
  k = sum(map(int, input().split()))
  if k < 20:
    ans += 1
print(ans)
          
      
