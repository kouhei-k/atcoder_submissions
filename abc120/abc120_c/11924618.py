d = dict()
d['0'] = 0
d['1'] = 0

S = input()

for x in S:
    d[x] += 1
print(min(d['0'], d['1'])*2)
