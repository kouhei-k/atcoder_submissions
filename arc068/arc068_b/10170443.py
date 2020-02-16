N = int(input())
A = list(map(int, input().split()))
A.sort()
s = set()
count = 0
for x in A:
    if x not in s:
        s.add(x)
    else:
        count += 1

if count % 2 == 0:
    print(len(s))
else:
    print(len(s) - 1)
