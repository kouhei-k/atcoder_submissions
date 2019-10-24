W,H=map(int,input().split())
import math
mod = 10**9+7
print(math.factorial(H+W-2)*pow(math.factorial(H-1),mod-2,mod)*pow(math.factorial(W-1),mod-2,mod)%mod)
