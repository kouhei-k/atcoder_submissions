a, b = input().split()
ansb = []
for i in range(int(a)):
    ansb.append(b)
ansa = []
for i in range(int(b)):
    ansa.append(a)
ansa = "".join(ansa)
ansb = "".join(ansb)
ans = [ansa, ansb]
ans.sort()
print(ans[0])
