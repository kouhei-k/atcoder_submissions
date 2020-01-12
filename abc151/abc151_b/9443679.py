N, K, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)

goal = M*N
if goal - S > K:
    print(-1)
else:
    print(max(0, goal - S))
