import math
X=int(input())
k=int(((2*X)**(0.5)))
X-=(k*(k+1))//2
print(k+math.ceil(X/k))
