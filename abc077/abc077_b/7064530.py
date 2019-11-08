import math
N = int(input())

n = math.sqrt(N)

if n == math.floor(n):
    print(N)

else:
    print(pow(math.floor(n), 2))
