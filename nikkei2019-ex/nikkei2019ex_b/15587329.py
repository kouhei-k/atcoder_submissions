N = int(input())
ans = 0
for i in range(10**5):
  if i**2 <= N:
    ans = i
  else:
    break
print(ans)
