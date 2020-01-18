S = input()
id = 0
keyence = "keyence"
for i in range(len(S)):
    if S[i] == keyence[id]:
        id += 1
    else:
        break
id2 = 1
for i in reversed(range(id, len(S))):
    if S[i] == keyence[-id2]:
        id2 += 1
    else:
        break

if id + id2 - 1 >= 7:
    print("YES")
else:
    print("NO")
