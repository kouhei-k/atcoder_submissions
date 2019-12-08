def int_ceil(x):
  last=int(str(x)[-1])
  return([x+10-last,last])

dishes =[0]*5
min=10
for i in range(5):
  x=(int(input()))
  if x % 10 != 0:
    ceiled=int_ceil(x)
    if ceiled[1] < min:
      min=ceiled[1]
    dishes[i]=ceiled[0]
  else:
    dishes[i]=x
print(sum(dishes) - 10 + min)
