import copy
S = input()
Slen = len(S)

Sc=[0]*Slen
for i in range(Slen):
    if S[i:i+2] == 'RL':
        for j in range(i,-1,-1):
            if S[j]=='R':
                Sc[(i-j)%2 + i] += 1
            else:
                break
        for j in range(i+1,Slen):
            if S[j] == 'L':
                Sc[(j-i)%2 +i] += 1
            else:
                break    

print(" ".join(map(str,Sc)))
