A = []
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
A.sort()
B = []
B.append(int(input()))
B.append(int(input()))
B.sort()
print(sum(A[1:])+B[-1])
