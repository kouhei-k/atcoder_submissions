N = input()
lenN = len(N)
N = int(N)
ans = 0
ans_list = []
for i in range(max(0, N - lenN*9), N+1):

    if i + sum(list(map(int, list(str(i))))) == N:
        ans += 1
        ans_list.append(i)
print(ans)
for x in ans_list:
    print(x)
