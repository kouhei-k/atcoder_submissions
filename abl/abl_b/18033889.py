A,B,C,D = map(int, input().split())
if A <= C:
  if B>=C:
 	 print("Yes")
  else:
    print("No")
elif D >= A:
  print("Yes")
else:
  print("No")
