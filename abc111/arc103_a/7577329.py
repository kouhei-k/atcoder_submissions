import collections
n = int(input())
v = list(map(int, input().split()))

odd = collections.defaultdict(int)

even = collections.defaultdict(int)

for i in range(n):
    if i % 2 == 0:
        even[v[i]] += 1

    else:
        odd[v[i]] += 1

even = list(even.items())
odd = list(odd.items())

even.sort(key=lambda x: x[1], reverse=True)
odd.sort(key=lambda x: x[1], reverse=True)

if even[0][0] == odd[0][0]:
    if len(even) == 1 and len(odd) == 1:
        print(n // 2)
    elif len(even) == 1:
        print(n - (even[0][1] + odd[1][1]))
    elif len(odd) == 1:
        print(n - (even[1][1] + odd[0][1]))
    else:
        print(min(n - (even[1][1] + odd[0][1]),
              n - (even[0][1] + odd[1][1])))
else:
    print(n - (even[0][1] + odd[0][1]))
