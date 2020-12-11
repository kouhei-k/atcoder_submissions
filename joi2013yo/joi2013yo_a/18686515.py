L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

import math
X = max(math.ceil(A/C),math.ceil(B/D))
print(max(0,L - X))
