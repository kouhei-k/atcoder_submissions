c1=input()
c2=input()
for i in range(3):
  if c1[i]==c2[-1-i]:
    continue
  else:
    print("NO")
    exit(0)
print("YES")
