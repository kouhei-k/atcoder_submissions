N=int(input())
a=list(map(int,input().split()))
count4=0
countodd=0
for i in range(N):
  if a[i]%2==1:
    countodd+=1
  elif a[i]%4==0:
    count4+=1
if countodd + count4 == N:
  if countodd <= count4+1:
    print("Yes")
  else:
    print("No")
else:
  if countodd <= count4:
    print("Yes")
  else:
    print("No")
