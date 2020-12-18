N = int(input())
M = int(input())
A = list(map(int, input().split()))
score = [0]*N
for i in range(M):
  B = list(map(int, input().split()))
  count = 0
  x = A[i]
  for j in range(N):
    if B[j] == x:
      score[j] += 1
    else:
      count += 1
  score[x-1] += count

      
print(*score, sep = '
')
  
