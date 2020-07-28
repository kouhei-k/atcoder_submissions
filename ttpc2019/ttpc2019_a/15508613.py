A,B,T = map(int, input().split())
d = B - A
Y = B
while(Y < T):
  Y += d
print(Y)
