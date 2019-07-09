import collections
S = input()

even = collections.defaultdict(int)
odd = collections.defaultdict(int)

for i in range(len(S)):
    if i % 2 == 0:
        odd[S[i]] += 1
    else:
        even[S[i]] += 1

odd = list(odd.keys())
even = list(even.keys())

if "R" in odd:
    if odd.index("R") >= 0:
        odd.pop(odd.index("R"))
if "U" in odd:
    if odd.index("U") >= 0:
        odd.pop(odd.index("U"))
if "D" in odd:
    if odd.index("D") >= 0:
        odd.pop(odd.index("D"))

if len(odd) != 0:
    print("No")
    exit(0)

if "L" in even:
    if even.index("L") >= 0:
        even.pop(even.index("L"))
if "U" in even:
    if even.index("U") >= 0:
        even.pop(even.index("U"))
if "D" in even:
    if even.index("D") >= 0:
        even.pop(even.index("D"))

if len(even) != 0:
    print("No")
else:
    print("Yes")
