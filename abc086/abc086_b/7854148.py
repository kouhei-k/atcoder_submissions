a,b = input().split()
ab = int(a+b)
i = 0
while(1):
  if i**2 == ab:
    print("Yes")
    exit(0)
  elif i**2 > ab:
    break
  i+= 1
print("No")
