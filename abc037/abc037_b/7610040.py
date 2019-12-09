N,Q = map(int, input().split())
L = [0] * Q
R = [0] * Q
T = [0] * Q
arr = [0] * N
for i in range(Q):
  L, R, T = map(int, input().split())
  arr[L-1:R] = [T] * (R - L + 1)
  
for i in range(N):
  print(arr[i])
