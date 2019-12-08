import collections
import math
N,A,B  = map(int, input().split())
v = list(map(int,input().split()))

nums = collections.defaultdict(int)
for x in v:
    nums[x] += 1
ave = [[0 for i in range (B - A + 1)] for j in range(2)]
v.sort(reverse = True)
for i in range(A , B + 1):
    ave[0][i - A] = sum(v[:i]) / i
    ave[1][i - A] = v[:i]
ans = max(ave[0])
print(ans)

indexes = [i for i in range(B - A + 1) if ave[0][i] == ans]
max_counter = [] * len(indexes)
ans = 0
for i in indexes:
    counter = collections.Counter(ave[1][i])
    tmp_ans = 1
    for x in counter:
        tmp_ans *= math.factorial(nums[x]) // math.factorial(counter[x]) // math.factorial(nums[x] - counter[x])
    ans += tmp_ans
print(ans)
