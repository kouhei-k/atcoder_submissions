N,T = map(int, input().split())
prev = 0
ans = 0
tt = list(map(int, input().split()))
for t in tt:
  if prev+T <= t:
    ans += T
  else:
    ans += (t - prev)
  prev = t

print(ans + T)
    
