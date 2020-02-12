N=int(input())
S=input()

def z_algo(S):
    N = len(S)
    A = [0]*N
    i = 1; j = 0
    A[0] = l = len(S)
    while i < l:
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A

s=[[0]*N for i in range(N)]
k=0
for k in range(N):
  s[k]= [0]*k + z_algo(S[k:])

ans=0
for i in range(N):
  for j in range(i+1,N):
    if s[i][j]+i > j:
      ans = max(ans,j - i)
    else:
      ans=max(s[i][j],ans)
    
print(ans)
      
 
 
