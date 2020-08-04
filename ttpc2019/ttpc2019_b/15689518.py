N = int(input())
for _ in range(N):
  s = input()
  if 'okyo' in s:
    id = s.index('okyo')
    if 'ech' in s[id+4:]:
      print('Yes')
    else:
      print("No")
  else:
    print('No')
