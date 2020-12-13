W,H,N = map(int, input().split())
px, py = map(int, input().split())
ans = 0
for _ in range(N-1):
  x,y = map(int, input().split())
  dx = (x-px)
  dy = (y-py)
  if dx*dy >= 0:
    ans += max(abs(dx), abs(dy))
    px = x
    py = y
  elif dx*dy < 0:
    ans += abs(dx) + abs(dy)
    px = x
    py = y
print(ans)
    
  
  


  
