A,B,C,D=map(int,input().split())
import fractions
lcm=C*D//fractions.gcd(C,D)

c=B // C - (A-1)//C
d=B//D - (A-1)//D
cd=B//lcm - (A-1)//lcm

print(B-A+1 - (c+d-cd))
