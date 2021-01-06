H,W,N = map(int, input().split())
S = [input() for i in range(H)]
import collections
from itertools import permutations

P = dict()
for i in range(H):
  for j in range(W):
    try:
      x = int(S[i][j])
      P[x] = (i,j)
    except:
      if S[i][j] == 'S':
        P[0] = (i,j)
D = [[0]*N for i in range(N)]
    
ans = 0
for i in range(N):
  s = set()
  q = collections.deque()
  s.add(P[i])
  q.append((P[i][0],P[i][1], 0))
  while(q):
    x, y, c = q.popleft()
    if S[x][y] == str(i+1):
      ans += c
      break
    for x2,y2 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
      if 0<=x2<H and 0<=y2<W:
        if S[x2][y2] == 'X':
          continue
        elif (x2,y2) not in s:
          s.add((x2,y2))
          q.append((x2,y2,c+1))
print(ans)
