S=input()

for i in reversed(range(len(S) - 1)):
  if i % 2 == 1:
    moji1 = S[0:(i//2) + 1]
    moji2 = S[(i//2) + 1: i+ 1]
    
    if moji1==moji2:
      print(i+1)
      break
