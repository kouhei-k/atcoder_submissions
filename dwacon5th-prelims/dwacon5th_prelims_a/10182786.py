N = int(input())
a = list(map(int, input().split()))
ave = sum(a) / N
diff = 10**9
ans=0
for i,x in enumerate(a):
  if diff > abs(ave - x):
    diff = abs(ave - x)
    ans = i
print(ans)
