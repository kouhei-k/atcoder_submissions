A, B = map(int, input().split())
ans = 0
for i in range(A, B+1):
    kaibun = str(i)
    for j in range(len(kaibun) // 2):

        if kaibun[j] != kaibun[-1-j]:
            break
        elif j == (len(kaibun) // 2) - 1:
            ans += 1
print(ans)
