H1, M1, H2, M2, K = map(int, input().split())

h = H2 - H1
m = M2 - M1
ans = h * 60 + m
print(max(0, ans - K))
