S = input()
p = int(S[:2])
s = int(S[2:])

if (p > 12 or p == 0) and (s <= 12 and s > 0):
  print("YYMM")
elif (p > 0 and p <= 12) and (s > 12 or s == 0):
  print("MMYY")
elif p < 13 and s < 13 and p > 0 and s > 0:
  print("AMBIGUOUS")
else:
  print("NA")
