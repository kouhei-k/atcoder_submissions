N, M = map(int, input().split())
ans = 0
if N >= 3:
    if M >= 3:
        ans = (N-2)*(M-2)
    else:
      if M == 2:
        ans=0
      else:
        ans=N-2
else:
    if N == 2:
      ans=0
    else:
      if M == 2:
        ans=0
      elif M == 1:
        ans=1
      else:
        ans=M-2
print(ans)
