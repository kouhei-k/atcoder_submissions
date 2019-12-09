import collections
H, W = map(int, input().split())
table = collections.defaultdict(int)
for i in range(H):
    for x in input():
        table[x] += 1

tmp = 0

for x in table:
    if table[x] % 2 == 1:
        table[x] -= 1
        tmp += 1
num = [0, 0]
for x in table:
    num[1] += table[x] // 4
    if table[x] % 4 != 0:
        num[0] += 1


if H % 2 == 1 and W % 2 == 1:
    if tmp != 1:
        print("No")
        exit(0)
    else:
        if H+W - 2 < num[0] * 2:
            print("No")
            exit(0)
        else:
            if ((H+W - 2) - num[0]*2) % 4 != 0:
                print("No")
                exit(0)

elif H % 2 == 1 or W % 2 == 1:
    if tmp != 0:
        print("No")
        exit(0)
    else:
        if W % 2 == 1:
            H, W = W, H
        if W < num[0]*2:
            print("No")
            exit(0)
        else:
            if (W - num[0]*2) % 4 != 0:
                print("No")
                exit(0)

else:
    if num[0] != 0 or tmp != 0:
        print("No")
        exit(0)


print("Yes")
