N = int(input())
s = set()

flag = True
for i in range(N):
    S = input()
    if S in s:
        flag = False
    if i > 0 and S[0] != prev:
        flag = False
    s.add(S)
    prev = S[-1]
if flag:
    print("Yes")
else:
    print("No")
