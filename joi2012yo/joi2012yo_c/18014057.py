N = int(input())
A, B = map(int, input().split())
C = int(input())
c = 0
D = [int(input()) for i in range(N)]
D.sort(reverse=True)

S = A
s = C
ave = C / A

for i in range(N):
    if ave < (s + D[i]) / (S + B):
        s += D[i]
        S += B
        ave = s / S
print(int(ave))
