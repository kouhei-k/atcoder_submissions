import math
N=int(input())
A=list(map(int,input().split()))
A=[x for x in A if x>0]
print(math.ceil(sum(A)/len(A)))
