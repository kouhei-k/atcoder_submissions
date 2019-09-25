import collections
N = int(input())
ans = 0
ans_table = collections.defaultdict(int)
prev = []
for i in range(1, N+1):

    tmp = i
    for j in range(2, int((i**0.5//1))+1):
        if tmp % j == 0:
            count = 0
            while tmp % j == 0:
                count += 1
                tmp = tmp//j
            ans_table[j] += count
    if tmp != 1:
        ans_table[tmp] += 1

ans_list = list(ans_table.values())
ans = 1
for x in ans_list:
    ans *= (x+1)

print(ans % ((10**9) + 7))
