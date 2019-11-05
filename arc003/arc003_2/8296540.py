N=int(input())
s=[input() for i in range(N)]
s2=[[s[i][::-1],i] for i in range(N)]
s2.sort()
for i in range(N):
  print(s[s2[i][1]])
