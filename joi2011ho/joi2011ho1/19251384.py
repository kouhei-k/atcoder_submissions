import sys
import numpy as np
readline = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
M,N=map(int,readline().split())
K=int(readline())
S=np.zeros((M+1,N+1),"S1")
for i in range(1,M+1):
  S[i,1:] = np.frombuffer(readline().rstrip(),'S1')

abcd=np.array(read().split(),np.int32)
J = (S==b'J').cumsum(axis=0).cumsum(axis=1)
O = (S==b'O').cumsum(axis=0).cumsum(axis=1)

a=abcd[0::4] - 1
b=abcd[1::4] - 1
c=abcd[2::4]
d=abcd[3::4]

J = J[c,d] + J[a,b] - J[a,d] - J[c,b] 
O = O[c,d] + O[a,b] - O[a,d] - O[c,b] 
I = (c-a)*(d-b) - J - O

print("
".join(["{} {} {}".format(j, o, i) for j, o, i in zip(J, O, I)]))
