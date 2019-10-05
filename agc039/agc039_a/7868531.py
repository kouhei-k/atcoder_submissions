S = input()
K = int(input())
flag = False
count = 0
for i in range(len(S)-1):
    if not flag:
        if S[i] == S[i+1]:
            count += 1
            flag = True
    else:
        flag = False
ans = 0

if len(S) == 1:
    ans = K // 2
elif S.count(S[0]) == len(S) and len(S) % 2 == 1:
    ans += count
    ans += (count + count + 1) * (K // 2)
elif S[0] == S[-1] and not flag:
    ans += count
    count = 0
    for i in range(1, len(S)-1):
        if not flag:
            if S[i] == S[i+1]:
                count += 1
                flag = True
        else:
            flag = False
    ans += (count + 1)*(K-1)

else:
    ans = count * K
print(ans)
