O = input()
E = input()
ans = [""]*(len(O) + len(E))
for i in range(len(ans)):
    if i % 2 == 0:
        ans[i] = O[i // 2]
    else:
        ans[i] = E[i // 2]
print("".join(ans))
