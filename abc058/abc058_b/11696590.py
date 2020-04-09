O = input()
E = input()
lo = len(O)
le = len(E)
ans = []
for a, b in zip(O, E[:min(le, lo)]):
    ans.append(a)
    ans.append(b)
if le < lo:
    ans.append(O[-1])

print("".join(ans))
