N,M,X=map(int,input().split())
A=list(map(int,input().split()))
left = [A[i] for i in range(M) if A[i] < X ]
right = [A[i] for i in range(M) if A[i] > X]
print(min(len(left),len(right)))
