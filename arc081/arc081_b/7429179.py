N = int(input())
S1 = list(input())
S2 = list(input())
ans=1
prev=0
ue = ""
for i in range(N):
  if S1[i]==S2[i]:
    if prev == 0:
      ans*=3
    elif prev == 1:
      ans*=2
    else:
      ans*=1
    prev = 1
  else:
    if ue == S1[i]:
      continue
    else:
      if prev == 0:
        ans*=6
      elif prev == 1:
        ans*=2
      else:
        ans*=3
      ue=S1[i]
      prev=2
print(ans%1000000007)
