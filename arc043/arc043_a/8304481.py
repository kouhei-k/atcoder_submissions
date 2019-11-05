N, A, B = map(int, input().split())
S = [int(input()) for i in range(N)]

maxS = max(S)
minS = min(S)
diff = max(S) - min(S)
P = 1
if diff == 0:
    if B != 0:
        print(-1)
        exit(0)
else:
    P = B / diff
ave = (sum(S) / N)*P

Q = A - ave

print(P, Q)
