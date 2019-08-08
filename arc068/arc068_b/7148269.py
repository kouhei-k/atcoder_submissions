import collections
counter = collections.defaultdict(int)
N = int(input())
A = input().split()

count = 0
for x in A:
    counter[x] += 1

for x in counter:
    if counter[x] != 1:
        count += counter[x] - 1

if count % 2 == 0:
    print(N - count)
else:
    print(N - (count + 1))
