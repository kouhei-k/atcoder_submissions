S = input()
K = int(input())
for x in S:
    x = int(x)
    if x != 1:
        print(x)
        break
    else:
        if K == 1:
            print(x)
            break
        else:
            K -= 1
