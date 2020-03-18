s = input()
t = input()
ss = s+ s
if len(s) != len(t):
  print(-1)
else:
  id = ss.rfind(t)
  if id > 0:
    print(len(s) - id)
  else:
    print(id)
