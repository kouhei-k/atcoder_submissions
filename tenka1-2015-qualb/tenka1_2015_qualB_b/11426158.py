S=input()
if len(S)==2:
  print("dict")
else:
  S=S[1:-1]
  counter=0
  for x in S:
    if x == "{":
      counter+=1
    elif x== "}":
      counter-=1
    elif counter==0 and x==":":
      print("dict")
      exit(0)
  print("set")
