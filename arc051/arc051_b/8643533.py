K=int(input())
fib=[1]*(K+1)
for i in range(2,K+1):
  fib[i]=fib[i-2]+fib[i-1]
print(fib[K-1],fib[K])
