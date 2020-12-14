A=int(input())
B=int(input())
C=int(input())
D=int(input())
P=int(input())
ans=A*P
P-=C
if P<0:
  P=0
print(min(ans,B+P*D))
