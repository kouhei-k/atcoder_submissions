N = int(input())
D = list(map(int, input().split()))


D.sort()
ans = [0]
ans = [D[i]
       for i in range(N) if i % 2 == 0] + [24 - D[i] for i in reversed(range(N)) if i % 2 == 1]

ans = [0] + ans + [0]

ans = [abs(ans[i+1] - ans[i]) for i in range(N+1)]

print(min(ans))
