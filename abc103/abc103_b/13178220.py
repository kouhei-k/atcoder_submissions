S = input()
T = input()
N = len(S)
for i in range(N):
    if S[i:]+S[:i] == T:
        print("Yes")
        exit(0)
print("No")
