N=list(map(int,list(input())))[::-1]
l=len(N)
b=sum([N[i] for i in range(l) if i %2==0])
a=sum([N[i] for i in range(l) if i %2==1])
print(a,b)
