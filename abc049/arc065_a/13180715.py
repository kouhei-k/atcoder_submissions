S = input()

s = ['dream', 'dreamer', 'erase', 'eraser']
R = len(S)
while(R > 0):
    for i in range(4):
        if R >= len(s[i]):
            if S[R-len(s[i]):R] == s[i]:
                R -= len(s[i])
                break
        if i == 3:
            print("NO")
            exit(0)
print("YES")
