import collections
N = int(input())
A = list(map(int, input().split()))


dic = collections.defaultdict(int)

for x in A:
    dic[x] += 1

dic = list(dic.items())
dic = [x for x in dic if x[1] >= 2]
dic = sorted(dic, reverse=True, key=lambda x: x[0])

if len(dic) >= 2:
    if dic[0][1] >= 4:
        print(dic[0][0] * dic[0][0])
    else:
        print(dic[0][0] * dic[1][0])
else:
    print(0)
