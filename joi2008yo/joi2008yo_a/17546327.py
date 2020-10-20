x = 1000 - int(input())
ans = 0
if x >= 500:
  ans += 1
  x -= 500
if x >= 100:
  ans += x // 100
  x = x % 100
if x >= 50:
  ans += x // 50
  x = x % 50
if x >= 10:
  ans += x // 10
  x = x % 10
if x >= 5:
  ans += 1
  x -= 5
ans += x
print(ans)
  
