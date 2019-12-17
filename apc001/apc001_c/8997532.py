N = int(input())
print(0)
res = input()
if res == "Vacant":
    exit(0)

print(N-1)
res2 = input()
if res2 == "Vacant":
    exit(0)
seat = [""]*N
seat[0] = res
seat[N-1] = res

first = 0
last = N-1

for i in range(18):
    ret = (first + last) // 2
    if ret == first:
        ret += 1
    print(ret)
    res = input()
    seat[ret] = res
    if res == "Vacant":
        exit(0)
    else:
        if (res == seat[first] and (ret - first) % 2 == 0) or (res != seat[first] and (ret - first) % 2 == 1):
            first = ret
        else:
            last = ret-1
