from itertools import permutations
Q, H, S, D = map(int, input().split())
N = int(input())*4

ans = 0
s = [(Q, 1), (H, 2), (S, 4), (D, 8)]

ans = float("inf")
for x in permutations(s):
    tmp = 0
    n = N
    for a, b in x:
        tmp += (n // b)*a
        n %= b
    ans = min(ans, tmp)
print(ans)
