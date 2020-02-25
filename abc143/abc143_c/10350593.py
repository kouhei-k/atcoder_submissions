N=int(input())
S=input()
S=[i for i in range(N) if i==0 or S[i]!=S[i-1]]
print(len(S))
