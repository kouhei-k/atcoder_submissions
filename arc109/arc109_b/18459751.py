n = int(input())
import math
x = 2*(n+1)

for i in range(int(n**0.5),int(x**0.5)+1):
    if (i+1)**2 + i + 1 > x:
        print(n+1 - i)
        exit(0)


       
