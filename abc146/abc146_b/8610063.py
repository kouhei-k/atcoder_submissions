N = int(input())
S = list(input())
n = len(S)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    id = alphabet.index(S[i])
    if id + N <= 25:
        S[i] = alphabet[id+N]
    else:

        S[i] = alphabet[(id+N)-26]

print("".join(S))
