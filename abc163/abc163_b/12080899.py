N, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)

if S > N:
    print(-1)
else:
    print(N-S)
