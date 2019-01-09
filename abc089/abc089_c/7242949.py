import fractions
import itertools
N = int(input())
M =[]
A = []
R = []
C = []
H = []


for i in range(N):
    name = input()
    initial = name[0]
    if initial == "M":
        M.append(name)
    elif initial == "A":
        A.append(name)
    elif initial == "R":
        R.append(name)
    elif initial == "C":
        C.append(name)
    elif initial == "H":
        H.append(name)

count = 0
S = []
if len(M) > 0:
    S.append(len(M))
if len(A) > 0:
    S.append(len(A))
if len(R) > 0:
    S.append(len(R))
if len(C) > 0:
    S.append(len(C))
if len(H) > 0:
    S.append(len(H))

if len(S) < 3:
    print("0")
    exit(0)

a = itertools.combinations(S,3)
ans = 0
for x in list(a):
    tmp = 1
    for y in x:
        tmp *= y
    ans += tmp
print(ans)
