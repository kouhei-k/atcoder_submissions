C = input()

a = "abcdefghijklmnopqrstuvwxyz"
d = dict()
for i, x in enumerate(a):
    d[x] = i+1
print(a[d[C]])
