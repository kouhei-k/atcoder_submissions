N=int(input())
L=len(str(N))
ans=(L-1)*9
ans+=int(str(N)[0])
tmp=[str(N)[0]] + ["9"]*(L-1)
tmp=int("".join(tmp))
if tmp>N:
  ans-=1
print(ans)
