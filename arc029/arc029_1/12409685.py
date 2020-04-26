N=int(input())
t=[int(input()) for i in range(N)]
t.sort(reverse=True)
x=0
y=0

for z in t:
  if x <= y:
    x+=z
  else:
    y+=z
print(max(x,y))
