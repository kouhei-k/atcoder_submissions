def divisors_sum(n):
    ret=0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ret+=i
            if i != n // i:
                ret+=n//i
    return(ret)
  
N=int(input())
ans=divisors_sum(N)
ans-=N
if N==ans:
  print("Perfect")
elif N>ans:
  print("Deficient")
else:
  print("Abundant")
