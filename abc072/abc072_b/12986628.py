s = input()
ans = [s[i] for i in range(len(s)) if i % 2 == 0]
print(''.join(ans))
