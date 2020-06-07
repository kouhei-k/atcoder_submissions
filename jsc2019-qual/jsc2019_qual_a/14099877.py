M,D = map(int, input().split())
ans = 0
for i in range(1,M+1):
  for j in range(2, D//10 + 1):
    for k in range(2, 10):
      if j*10 + k > D:
        break
      else:
        if j*k == i:
          ans += 1
print(ans)
