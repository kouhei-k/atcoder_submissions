N=int(input())
for i in range(1,101):
  if i**3==N:
    print("YES")
    exit(0)
print("NO")
