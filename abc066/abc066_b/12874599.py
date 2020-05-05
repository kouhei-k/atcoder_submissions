S = input()
N = len(S)
for i in range(N-1, -1, -2):
    if S[:i//2] == S[i//2:i-1]:
        print(i-1)
        exit(0)
