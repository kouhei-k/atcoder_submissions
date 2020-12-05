import math

N = int(input())
X = 10**10
T = input()

ans = 0
c = math.ceil(N/3)
S = '110'


for i in range(3):
    flag = True
    for j in range(N):
        if S[(i+j) % 3] == T[j]:
            continue
        else:
            flag = False
            break

    if flag:
        ans += X - (math.ceil((i+N)/3)-1)

print(ans)
