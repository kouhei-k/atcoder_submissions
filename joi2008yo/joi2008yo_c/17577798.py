n = int(input())
s = set([i for i in range(1, 2*n+1)])
c = [2 for i in range(n*2)]


for i in range(n):
    x = int(input())
    c[x-1] = 1

flag = True
i = 0
taro = n
jiro = n
next = False
while(taro != 0 and jiro != 0):
    if flag:
        while(c[i] != 1):
            i += 1
            if i == 2*n:
                i = 0
                flag = False
                next = True
                break
        if next:
            next = False
            continue
        c[i] = 0
        flag = False
        taro -= 1
    else:
        while(c[i] != 2):
            i += 1
            if i == 2*n:
                i = 0
                flag = True
                next = True
                break
        if next:
            next = False
            continue
        c[i] = 0
        flag = True
        jiro -= 1
    if taro == 0 or jiro == 0:
        break

print(jiro)
print(taro)
