S = list(input())
count = [0, 0]
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "0":
            count[0] += 1
        else:
            count[1] += 1
    else:
        if S[i] == "1":
            count[0] += 1
        else:
            count[1] += 1
print(min(count))
