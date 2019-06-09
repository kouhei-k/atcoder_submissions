L,R = map(int,input().split())
ans = 2019

if R*(R-1)<2019:
  print(R*(R-1))
  exit(0)
else:
  if R == L+1:
    print((R*L)%2019)
    exit(0)
  else:
    r =673 - L % 673
    if L+r <= R:
      print("0")
      exit(0)
    else:
      for i in range(L,R+1):
        for j in range(i+1,R+1):
          if (i*j)%2019 < ans:
            ans = (i*j) % 2019
            if ans == 0:
              break
print(ans)
