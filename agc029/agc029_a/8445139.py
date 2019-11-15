S = input()
tmp = []
count = 1
for i, x in enumerate(S):
    if x == 'B':
        tmp.append([i, count])
        count += 1

tmp.sort(key=lambda x: x[1], reverse=True)
ans = 0
for i in range(len(tmp)):
    x = tmp[i][0]
    ans += len(S)-1-i - x
print(ans)
