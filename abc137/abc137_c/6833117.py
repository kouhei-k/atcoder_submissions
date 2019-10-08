from collections import defaultdict
Sdic = defaultdict(int)

N = int(input())
S = ['']* N
ans = 0
for i in range(N):
    Sdic[str(sorted(input()))] += 1

for i in Sdic.keys():
    ans += (Sdic[i] * (Sdic[i] - 1)) // 2

print(ans)
