T = input()
prev = ''
ans = []
N = len(T)
for i, x in enumerate(T):
    if x == '?':
        ans.append("D")

    else:
        ans.append(x)
print(''.join(ans))
