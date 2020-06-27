S = input()
T = input()

ans = 0
for a, b in zip(S, T):
    if a != b:
        ans += 1
print(ans)
