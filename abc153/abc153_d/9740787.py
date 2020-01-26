import math
H = int(input())


ans = 0
count = 1
while(H > 0):
    ans += count
    H = H // 2
    count *= 2
print(ans)
