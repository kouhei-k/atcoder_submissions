x,y=input().split()
group=[["1","3","5","7","8","10","12"],["4","6","9","11"],["2"]]
for i in range(3):
  if x in group[i]:
    if y in group[i]:
      print("Yes")
    else:
      print("No")
    break
