s=input()
t=input()
ss=s+s
n=len(s)
for i in range(n):
  if ss[i:i+n]==t:
    print("Yes")
    exit(0)

print("No")
