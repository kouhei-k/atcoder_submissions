s=list(input())
N=len(s)
s1=s[:N//2]
s2=s[-(N//2):]
s2=s2[::-1]
for i in range(N//2):
  if s1[i]=="*" or s2[i]=="*":
    continue
  if s1[i]!=s2[i]:
    print("NO")
    exit(0)
print("YES")
