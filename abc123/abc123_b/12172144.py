import math
abcde = [int(input()) for i in range(5)]

abcde.sort(key=lambda x: (x % 10))

flag = False
ans = 0
for x in abcde:
    if x % 10 == 0 or flag:
        if x % 10 == 0:
            ans += x
        else:
            ans += ((x//10)+1)*10
    else:
        ans += x
        flag = True
print(ans)
