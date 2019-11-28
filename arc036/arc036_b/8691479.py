N=int(input())
A=[int(input()) for i in range(N)]
left=[0]*N
right=[0]*N
for i in range(1,N):
  if A[i]>A[i-1]:
    left[i]=left[i-1]+1
  else:
    continue
for i in reversed(range(N-1)):
  if A[i]>A[i+1]:
    right[i]=right[i+1]+1
  else:
    continue
S=[left[i]+right[i] for i in range(N)]
id = S.index(max(S))

print(max(S)+1)
