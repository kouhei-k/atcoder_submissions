import re
s = input()

flash = set(["10", 'J', 'Q', 'K', 'A'])

ans = [[] for i in range(4)]
mark = 'SHDC'
splitter = ['[HDC]', '[DCS]', '[CSH]', '[SHD]']
tmp = 0
for i, m in enumerate(mark):
    tmp = 0
    for X in s.split(m):
        X2 = re.split(splitter[i], X)
        x = X2[0]
        # print(x)
        if x in flash:
            tmp += 1
        elif x:
            ans[i] += mark[i] + x
        if tmp == 5:
            break
        ans[i] += X[len(x):]
    # print(ans)
ans.sort(key=lambda x: len(x))
if ans[0]:
    print(''.join(ans[0]))
else:
    print(0)
