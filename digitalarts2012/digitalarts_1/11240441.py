s = list(input().split())
N = int(input())
t = set([input() for i in range(N)])
ans = []
for x in s:
    flag = True
    for y in t:
        if len(y) == len(x):
            count = 0
            for a, b in zip(x, y):
                if b == "*" or a == b:
                    count += 1
                else:
                    break
            if count == len(x):
                flag = False
    if flag:
        ans.append(x)

    else:
        ans.append("*"*len(x))
print(*ans)
