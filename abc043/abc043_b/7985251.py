s=input()
buff=[]
for x in s:
  if x == "0" or x == "1":
    buff.append(x)
  else:
    if len(buff) > 0:
      buff.pop()
print("".join(buff))
