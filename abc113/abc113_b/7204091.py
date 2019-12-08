
N = int(input())
T,A = map(int,input().split())
def calc(A):
  return((T - A) / 0.006)

H = list(map(int,input().split()))
x = calc(A)
ans=max(H) - x
for i in range(N):
  if abs(H[i] - x) < abs(ans):
    ans = H[i] - x
    
ans = int(ans + x)
print(H.index(ans)+1)
