n=int(input())
ans=0
c=[0]*50
c[0]=1
c[1]=1
def fib(n):
  if c[n]:
    return(c[n])
  else:
    c[n]=fib(n-1)+fib(n-2)
    return(c[n])
print(fib(n))
