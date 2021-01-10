N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
for a, b in zip(A, B):
    S += a*b
if S:
    print("No")
else:
    print("Yes")
