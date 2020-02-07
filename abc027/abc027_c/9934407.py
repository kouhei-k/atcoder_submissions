N = int(input())
import math
x = 1
count = 0
while(x <= N):
    count += 1
    x *= 2
    if (math.log(N/x,2)%2>=1):
        x += 1

if count % 2 == 1:
    print("Aoki")
else:
    print("Takahashi")
 
