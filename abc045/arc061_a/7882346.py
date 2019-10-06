S = input()
ans = 0
for i in range(2**(len(S)-1)):
    tmp = []
    prev = 0
    for j in range(1, len(S)):
        if (i >> (j-1)) % 2 == 1:
            if len(S[prev:j]) != 0:
                tmp.append(int(S[prev:j]))
                prev = j
    if len(S[prev:]) != 0:
        tmp.append(int(S[prev:]))
    else:
        print(prev)
    ans += sum(tmp)
print(ans)
