N = int(input())
diff = 2025 - N
ans = []
for i in range(1, 10):
    if diff % i == 0 and diff // i < 10:
        ans.append([i, diff//i])
for i in range(len(ans)):
    print(" x ".join(map(str, ans[i])))
