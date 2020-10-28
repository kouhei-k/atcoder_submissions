from itertools import permutations
n = int(input())
k = int(input())
X = [input() for i in range(n)]
s = set()
for x in permutations(range(n), k):
    tmp = []
    for y in x:
        tmp.append(X[y])
    s.add(''.join(tmp))
print(len(s))
